	lw	0	1	six	load reg1 with 6
	lw	1	2	3	load reg2 with -1
start	add	1	2	1	decrement reg1
	beq	0	1	2	goto end of program when reg1==0
	beq	0	0	start	go back to the beginning of the loop
	noop
done	halt				end of program
six	.fill	6
six	.fill	6			it makes error that duplicate lable
neg1	.fill	-1
stAddr	.fill	start			will contain the address of start (2)
