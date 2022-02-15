#include <linux/init.h>
#include <linux/kernel.h>
#include <linux/module.h>
#include <linux/proc_fs.h>
#include <asm/uaccess.h>
#include <asm/param.h>

#define BUFFER_SIZE 128
#define PROC_NAME "seconds"

static unsigned long jiffie_start, jiffie_end ,time_elapsed;

ssize_t proc_read(struct file *file, char __user *usr_buf,size_t count, loff_t *pos);

static struct file_operations proc_ops ={
  .owner = THIS_MODULE,
  .read = proc_read,
};

/* This function is called when the module is loaded. */
int proc_init(void)
{
  /* creates the /proc/seconds entry */
  jiffie_start=jiffies;
  proc_create(PROC_NAME, 0666, NULL, &proc_ops);
  return 0;
}

/* This function is called when the module is removed. */
void proc_exit(void){

/* removes the /proc/seconds entry */
  remove_proc_entry(PROC_NAME, NULL);
}

/* This function is called each time /proc/seconds is read */
ssize_t proc_read(struct file *f, char  __user *usr_buf,size_t count, loff_t *pos)
{
  int rv = 0;
  char buffer[BUFFER_SIZE];
  static int completed = 0;

  if (completed) {
    completed = 0;
    return 0;
  }

  completed = 1;
  jiffie_end=jiffies;
  time_elapsed=jiffie_end-jiffie_start;

  rv = sprintf(buffer, "TIME ELAPSED : %lu \n",time_elapsted/HZ);

  /* copies kernel space buffer to user space usr_buf */
  if(copy_to_user(usr_buf, buffer, rv)){
		printk(KERN_ERR "failed to copy to user.\n");
	}

  return rv;
}
module_init(proc_init);
module_exit(proc_exit);

MODULE_LICENSE("GPL");
MODULE_DESCRIPTION("SECONDS MODULE");
MODULE_AUTHOR("SGG");
