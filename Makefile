a.out:main.c
	@gcc main.c -o a.out -g -lcurl
clean:
	@rm -rf a.out sh* sz*
