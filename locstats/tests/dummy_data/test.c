/* First-line comment */
#include <stdio.h>

/*****
 * multi
 * line
 * comment
*****/

int main (int argc, char * argv[])
{
    // Comment
    printf("This is some dummy code\n");

    // Another
    // comment // this shouldn't count as an extra comment /* neither should this */
    return 0; // Inline comment (shouldn't be removed)
}
