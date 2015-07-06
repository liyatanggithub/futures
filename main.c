#include <curl/curl.h>
#include <sys/time.h>
#include <stdio.h>
#include <signal.h>
#include <string.h>
#include <malloc.h>
#include <stdlib.h>
#include <unistd.h>
#pragma comment(lib, "libcurl.lib")
#define SOCKET_ERROR	-1
#define TIME_SCHEDULE	4

char FuturesUrl[100] = "http://hq.sinajs.cn/list=AG1512";
char ReciveText[220];
char TimeNow[35];
int CurlOk;
int NowPrice;
time_t start1,end1,start2,end2,start3,end3;

size_t write_data(char *buffer, size_t size, size_t nitems, void *outstream)
{
	sprintf(outstream,"%s",buffer);
	CurlOk=1;
	return 0;
}

int get_futures_data(char* p)
{
	char *pc;
	int i=0;
	if(CurlOk == 0)
		return -1;
	pc=strtok(p,", =_\"");
	while((pc=strtok(NULL,", =_\"")))
	{
		switch(i)
		{
			case 11:
				NowPrice = atol(pc);
				break;
			default:
				break;
		}
		i++;
	}
	return 0;
}

void get_futures_text()
{
	int MaxCount 	= TIME_SCHEDULE-1;
	int SelectReturn;
	int RunningHandleCount 	= 1;
	int MaxFd;
	fd_set FdRead;
	fd_set FdWrite;
	fd_set FdExcept;
	struct timeval tv;
	tv.tv_sec 	= 1;
	tv.tv_usec 	= 0;

	curl_global_init(CURL_GLOBAL_ALL);
	CURL* pCurl 	= curl_easy_init();
	curl_easy_setopt(pCurl, CURLOPT_WRITEDATA, (void*)ReciveText);
	curl_easy_setopt(pCurl, CURLOPT_WRITEFUNCTION, write_data);
	curl_easy_setopt(pCurl, CURLOPT_URL, FuturesUrl);

	CURLM* pCurlM 	= curl_multi_init();
	curl_multi_add_handle(pCurlM, pCurl);
	curl_multi_perform(pCurlM, &RunningHandleCount);
	while(RunningHandleCount)
	{
		FD_ZERO(&FdRead);
		FD_ZERO(&FdWrite);
		FD_ZERO(&FdExcept);
		curl_multi_fdset(pCurlM, &FdRead, &FdWrite, &FdExcept, &MaxFd);
		SelectReturn = select(MaxFd+1, &FdRead, &FdWrite, &FdExcept, &tv);
		if(SOCKET_ERROR == SelectReturn)
		{
			CurlOk = 0;
			break;
		}
		else if (0 == SelectReturn)
			MaxCount--;
		if(MaxCount==0)
		{
			CurlOk = 0;
			break;
		}

		curl_multi_perform(pCurlM, &RunningHandleCount);
		tv.tv_sec = 1;
		tv.tv_usec = 0;
	}
	curl_multi_remove_handle(pCurlM, pCurl);
	curl_easy_cleanup(pCurl);
	curl_multi_cleanup(pCurlM);
	curl_global_cleanup();
	get_futures_data(ReciveText);
	printf("%d\t%s",NowPrice,TimeNow);
}

void init_time()
{
	time_t now;
	struct tm timenow;

	time(&now);
	timenow = *localtime(&now);
	timenow.tm_hour = 9;
	timenow.tm_min = 0;
	timenow.tm_sec = 0;
	start1=mktime(&timenow);			//9:00
	end1=start1+9000;					//11:30
	start2=end1+7200;					//13:30
	end2=start2+5400;					//15:00
	start3=end2+21600;					//21:00
	end3=start3+19800;					//2:30
}

int time_is_on_trans()
{
	time_t now;
	struct tm *timenow;

	time(&now);
	timenow = localtime(&now);
	strcpy(TimeNow,asctime(timenow));
	if(((now>=start1)&&(now<=end1))||((now>=start2)&&(now<=end2))||((now>=start3)&&(now<=end3)))
		return 1;
	else if(now > end3)
		init_time();
	return 0;
}

void main()
{
	init_time();
	while(1)
	{
		if(time_is_on_trans())
			get_futures_text();
	}
}
