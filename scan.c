#include <stdio.h>
#include <stdlib.h>

void executeCommand(const char *command) {
    printf("Executing: %s\n", command);
    system(command);
}

void pingHost(const char *host) {
    char command[100];
    sprintf(command, "ping -c 1 %s", host);
    executeCommand(command);
}

void scanPorts(const char *host, int startPort, int endPort) {
    printf("Scanning ports on %s from %d to %d\n", host, startPort, endPort);
    for (int port = startPort; port <= endPort; ++port) {
        char command[100];
        sprintf(command, "nc -z -w 1 %s %d", host, port);
        int result = system(command);

        if (result == 0) {
            printf("Port %d is open\n", port);
        }
    }
}

void traceroute(const char *host) {
    char command[100];
    sprintf(command, "traceroute %s", host);
    executeCommand(command);
}

void fetchHTTPHeaders(const char *url) {
    char command[100];
    sprintf(command, "curl -I %s", url);
    executeCommand(command);
}

void niktoScan(const char *host) {
    char command[100];
    sprintf(command, "nikto -h %s", host);
    executeCommand(command);
}

void sqlmapScan(const char *url) {
    char command[100];
    sprintf(command, "sqlmap -u %s --dbs", url);
    executeCommand(command);
}

int main() {
    char host[50];
    printf("Enter IP address or domain name: ");
    scanf("%s", host);

    int choice;
    printf("Choose operation:\n1. Ping\n2. Scan Ports\n3. Traceroute\n4. Fetch HTTP Headers\n5. Nikto Scan\n6. SQLMap Scan\n");
    scanf("%d", &choice);

    switch (choice) {
        case 1:
            pingHost(host);
            break;
        case 2: {
            int startPort, endPort;
            printf("Enter starting port: ");
            scanf("%d", &startPort);
            printf("Enter ending port: ");
            scanf("%d", &endPort);

            scanPorts(host, startPort, endPort);
            break;
        }
        case 3:
            traceroute(host);
            break;
        case 4: {
            char url[100];
            printf("Enter URL for HTTP headers: ");
            scanf("%s", url);
            fetchHTTPHeaders(url);
            break;
        }
        case 5:
            niktoScan(host);
            break;
        case 6: {
            char url[100];
            printf("Enter URL for SQLMap: ");
            scanf("%s", url);
            sqlmapScan(url);
            break;
        }
        default:
            printf("Invalid choice\n");
            return 1;
    }

    return 0;
}
