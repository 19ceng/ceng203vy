#include <stdio.h>

void as10_s2(char *s);

int main(void) {
	int x = 5, y = 7;
	int i;
	char str[] = "bar";

	// s1
	y += x + y < 10;
	printf("y = %d\n", y);

	for (i=0; i<5; i++)
		printf("%c", 'a' + i);

	printf("\n");

	i = 99;
	while (i-- > 100) ;
	printf("i = %d\n", i);
	
	as10_s2(str);
	printf("str = %s\n", str);

	return 0;
}

void as10_s2(char s[]) {
	char *p = s;

	while (*s)
		s++;

	for (s--; s>p; s--, p++) {
		char c = *s;
		*s = *p;
		*p = c;
	}
}
