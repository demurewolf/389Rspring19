# Writeup 7 - Binaries I

Name: Josiah Wedgwood
Section: 0101

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: Josiah Wedgwood

## Assignment Writeup

### Part 1 (90 Pts)

*Put your code here as well as in main.c*
```c
/*
 * Name: Josiah Wedgwood
 * Section: 0101
 *
 * I pledge on my honor that I have not given or received any unauthorized
 * assistance on this assignment or examination.
 *
 * Digital acknowledgement: Josiah Wedgwood
 */

/* your code goes here */

#include <stdio.h>

int main() {
    int b = 0x1ceb00da;
    int a = 0xfeedface;
    int sp1, sp2;
    
    printf("a = %d\n", a);
    printf("b = %d\n", b);
    
    a = a ^ b;
    b = b ^ a;
    a = b ^ a;
    
    printf("a = %d\n", a);
    printf("b = %d\n", b);

    return 0;
}
```

### Part 2 (10 Pts)

The main.s program first prints two numbers, a = -17958194 (0xfeedface) and b = 485163226 (0x1ceb00da). It then swaps the values of a and b with three xor operations, and then re-prints the values held by a = 485163226 and b = -17958194. 
