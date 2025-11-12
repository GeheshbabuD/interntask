#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>    
#include <unistd.h>      

int main() {
    struct stat sfile;
    if (stat("stat.c", &sfile) == -1) {
        perror("stat failed");
        exit(1);
    }

    printf("file st_uid: %d\n", sfile.st_uid);
    printf("file st_gid: %d\n", sfile.st_gid);
    printf("file st_size: %ld bytes\n", sfile.st_size);
    printf("file st_blocks: %ld\n", sfile.st_blocks);
    printf("file serialno (inode): %ld\n", sfile.st_ino);
    printf("file recent access time: %ld\n", sfile.st_atime);
    printf("file permission change time: %ld\n", sfile.st_ctime);
    printf("file recent modified time: %ld\n", sfile.st_mtime);

    return 0;
}
