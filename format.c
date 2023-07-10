#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char FLAG[4096];
char temp[4096];

int menu(void){
    char buffer[40];
    int return_val;

    char space_punk[] = 
"    _____       __           __     ______        __       \n"
"   / ___/____ _/ /_____     / /_   / ____/____   / /_      \n"
"   \\__ \\/ __ `/ __/ __ \\   / __/  / / __ / __ \\ / __ \\     \n"
"  ___/ / /_/ / /_/ /_/ /  / /_   / /_/ // /_/ // / / /     \n"
" /____/\\__,_/\\__/\\____/   \\__/   \\____/ \\____//_/ /_/      \n";


    puts(space_punk);
    puts("[1] Transmit SOS");
    puts("[2] Celestial Info");
    puts("[3] Launch File");
    puts("[4] Retrieve File");
    puts("[5] Warp Out");
    printf("\nNebulaRogue > ");

    fgets(buffer, 40, stdin);
    return_val = atoi(buffer);
}

void server_status(void){
    system("uname -a");
    printf("\n");
    system("uptime");
}

void put_file(){
    char filename[40];
    puts("Example: launch test.txt");
    printf("Enter the file to embark upon: ");
    fgets(filename, 40, stdin);

    printf("You are initiating the cosmic voyage of ");
    printf(filename);
    printf("\n");
}

int main(){
    setbuf(stdin, 0);
    setbuf(stdout, 0);
    
    FILE *content;

    //Open config
    content = fopen("cosmic_config.txt", "r");

    if (content != NULL) {
        while (fgets(temp, sizeof(temp), content) != NULL) {
            strcat(FLAG, temp);
        }

        puts("Welcome to the Astro-FTP: A Spacepunk Odyssey for your interstellar abode. Still orbiting HEAVILY for development. Most features remain locked in stardust!!");
        puts("Embrace the cosmic FORMAT to elevate a developer's existence\n");

        do {
            int options = menu();
            switch(options){
                case 1:
                    break;
                case 2:
                    server_status();
                    break;
                case 3:
                    put_file();
                    break;
                case 4:
                    puts("WIP");
                    break;
                case 5:
                    puts("Engaging Hyperdrive... Farewell, fellow traveler");;
                    exit(0);
                default:
                    puts("Invalid coordinates.\n");
                    break;
            }
        } while(1);
    } else{
        puts("The void beckons... Departing now");
        exit(0);
    }
}