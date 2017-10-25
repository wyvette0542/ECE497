#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h> 
#include <signal.h>    // Defines signal-handling functions (i.e. trap Ctrl-C)
#include <unistd.h>

#define GPIO3_START_ADDR 0x481ae000
#define GPIO3_END_ADDR 0x481b0000
#define GPIO3_SIZE (GPIO3_END_ADDR - GPIO3_START_ADDR)

#define GPIO_OE 0x134
#define GPIO_DATAIN 0x138
#define GPIO_SETDATAOUT 0x194
#define GPIO_CLEARDATAOUT 0x190

#define GPIO_95 (1<<1)     // LED
#define GPIO_96 (1<<2)  // Button 

int keepgoing = 1;    // Set to 0 when ctrl-c is pressed

void signal_handler(int sig);
// Callback called when SIGINT is sent to the process (Ctrl-C)
void signal_handler(int sig)
{
	printf( "\nCtrl-C pressed, cleaning up and exiting...\n" );
	keepgoing = 0;
}

int main() {
	volatile void *gpio_addr;
	volatile unsigned int *gpio_datain;
	volatile unsigned int *gpio_oe_addr;
	volatile unsigned int *gpio_setdataout_addr;
	volatile unsigned int *gpio_cleardataout_addr;
	unsigned int reg;

	// Set the signal callback for Ctrl-C
	signal(SIGINT, signal_handler);

	int fd = open("/dev/mem", O_RDWR);

	gpio_addr = mmap(0, GPIO3_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, GPIO3_START_ADDR);

	gpio_oe_addr           = gpio_addr + GPIO_OE;
	gpio_setdataout_addr   = gpio_addr + GPIO_SETDATAOUT;
	gpio_cleardataout_addr = gpio_addr + GPIO_CLEARDATAOUT;
	gpio_datain          = gpio_addr + GPIO_DATAIN;

	int button;

	reg = *gpio_oe_addr;
	reg &= ~(GPIO_95);
	*gpio_oe_addr = reg;

	while (keepgoing) {
		button = (*gpio_datain) & GPIO_96;
		if (button) {
			*gpio_setdataout_addr = GPIO_95; 
		} else {
			*gpio_cleardataout_addr = GPIO_95;
		}
	}

	munmap((void *)gpio_addr, GPIO3_SIZE);
	close(fd);
	printf("close \n");
	return 0;
}