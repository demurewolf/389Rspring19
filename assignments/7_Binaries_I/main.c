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
