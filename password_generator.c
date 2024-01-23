#include <stdio.h>
#include <string.h>

void generate_passwords(char characters[], int length, char filename[]) {
    FILE *file = fopen(filename, "w");
    if (file == NULL) {
        printf("Error opening file.\n");
        return;
    }

    char password[length + 1];
    password[length] = '\0';

    for (int i = 0; i < length; ++i) {
        password[i] = characters[0];
    }

    do {
        fprintf(file, "%s\n", password);
        printf("%s\n", password);

        
        for (int i = length - 1; i >= 0; --i) {
            if (password[i] != characters[strlen(characters) - 1]) {
                int j;
                for (j = 0; j < strlen(characters); ++j) {
                    if (password[i] == characters[j]) {
                        break;
                    }
                }
                password[i] = characters[j + 1];
                break;
            } else {
                password[i] = characters[0];
            }
        }
    } while (password[0] != '\0');

    fclose(file);
}

int main() {
    char words[] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    char pins[] = "0123456789";

    int choice, length;
    printf("Choose the type of password to generate\n");
    printf("1. Words\n2. Pins\n3. Word-Pins combination\n");
    printf("Enter option ---> ");
    scanf("%d", &choice);

    printf("Enter the length of the password: ");
    scanf("%d", &length);

    char mix[strlen(words) + strlen(pins) + 1];

    switch (choice) {
        case 1:
            generate_passwords(words, length, "wordlist.txt");
            break;
        case 2:
            generate_passwords(pins, length, "pinlist.txt");
            break;
        case 3:
            strcpy(mix, words);
            strcat(mix, pins);
            generate_passwords(mix, length, "pinwords.txt");
            break;
        default:
            printf("Invalid choice.\n");
            return 1;
    }

    return 0;
}
