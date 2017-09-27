#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h> 
#include <signal.h>    // Defines signal-handling functions (i.e. trap Ctrl-C)
#include <unistd.h>

#define GPIO1_START_ADDR 0x4804C000
#define GPIO1_END_ADDR 0x4804e000
#define GPIO1_SIZE (GPIO1_END_ADDR - GPIO1_START_ADDR)

#define GPIO3_START_ADDR 0x481ae000
#define GPIO3_END_ADDR 0x481b0000
#define GPIO3_SIZE (GPIO3_END_ADDR - GPIO3_START_ADDR)

#define GPIO_OE 0x134
#define GPIO_DATAIN 0x138
#define GPIO_SETDATAOUT 0x194
#define GPIO_CLEARDATAOUT 0x190

#define USR2 (1<<23)     // LED left
#define USR3 (1<<24)     // LED right
#define GPIO_49 (1<<17)  // Button right
#define GPIO_113 (1<<17)  // Button left

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
	volatile void *gpio_addr_3;
	volatile unsigned int *gpio_datain;
	volatile unsigned int *gpio_datain_3;
	volatile unsigned int *gpio_oe_addr;
	volatile unsigned int *gpio_setdataout_addr;
	volatile unsigned int *gpio_cleardataout_addr;
	unsigned int reg;

	// Set the signal callback for Ctrl-C
	signal(SIGINT, signal_handler);

	int fd = open("/dev/mem", O_RDWR);

	gpio_addr = mmap(0, GPIO1_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, GPIO1_START_ADDR);
	gpio_addr_3 = mmap(0, GPIO3_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, GPIO3_START_ADDR);

	gpio_oe_addr           = gpio_addr + GPIO_OE;
	gpio_setdataout_addr   = gpio_addr + GPIO_SETDATAOUT;
	gpio_cleardataout_addr = gpio_addr + GPIO_CLEARDATAOUT;
	gpio_datain            = gpio_addr + GPIO_DATAIN;
	gpio_datain_3          = gpio_addr_3 + GPIO_DATAIN;

	int buttonL, buttonR;

	reg = *gpio_oe_addr;
	reg &= ~(USR3 | USR2);
	*gpio_oe_addr = reg;

	while (keepgoing) {
		buttonL = (*gpio_datain_3) & GPIO_113;
		buttonR = (*gpio_datain) & GPIO_49;
		if (buttonL) {
			*gpio_setdataout_addr = USR2; 
		} else {
			*gpio_cleardataout_addr = USR2;
		}
		if (buttonR) {
			*gpio_setdataout_addr = USR3; 
		} else {
			*gpio_cleardataout_addr = USR3;
		}
	}

	munmap((void *)gpio_addr, GPIO1_SIZE);
	munmap((void *)gpio_addr_3, GPIO1_SIZE);
	close(fd);
	printf("close \n");
	return 0;
}
