#include<linux/init.h>
#include<linux/module.h>
#include <linux/uaccess.h>
#include<linux/fs.h>
#include<linux/sched.h>
#include<linux/device.h>
#include<linux/slab.h>
#include <linux/proc_fs.h>
#include <linux/string.h>
#include <linux/timer.h>

#define BUFFER_SIZE 128
#define PROC_NAME "jiffies"

static int myInit(void);
static void myExit(void);

struct proc_dir_entry *my_proc;

/* Read operation on proc */
ssize_t seq_read(struct file *fp, char *buf, size_t len, loff_t * off)
{
/* Logic to read data once */
static int finished=0;
if(finished) {
finished=0;
return 0;
}
finished=1;

/* find out current value of jiffies */

sprintf(buf, "Value of jiffies %lu \n", jiffies);
return strlen(buf);
}

/* File operation on proc */
static struct proc_ops my_fpos = {
  .proc_read = seq_read,
};

/* Init of kernel module */
static int __init myInit(void)
{

/* Create proc file with name of jiffies */
my_proc = proc_create(PROC_NAME, 0666, NULL, &my_fpos);

if(my_proc == NULL){
printk(KERN_INFO "Error to create proc File\n");
return -1;
}

return 0;
}
/* exit of kernel module */
static void myExit(void)
{
remove_proc_entry("jiffies",NULL);
return;
}

module_init(myInit);
module_exit(myExit);

MODULE_LICENSE("GPL");
MODULE_DESCRIPTION("Jiffie Module");
MODULE_AUTHOR("SSG");
