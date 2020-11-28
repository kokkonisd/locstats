.data

message: .asciiz "\nHello, World!\n" # Test

.text

ori $v0, 4 # Hey
la $a0, message # Hello
syscall # Multi
        # line
        # comment

ori $v0, 10
syscall
