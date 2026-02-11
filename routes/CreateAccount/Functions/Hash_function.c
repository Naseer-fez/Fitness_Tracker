// #include <stdio.h>
#include <string.h>
#include <stdlib.h>
char avalibale[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                   "abcdefghijklmnopqrstuvwxyz"
                   "0123456789"
                   "!@#$^&*()_+-=[]{}|;:',.<>?/`~";
#define Hash_Size 257
#define allchars 91

int seedgenerator(char *user, char *password);
char *Hashreturn(char *user, char *password);
void randomcharacterfill(char *password, char *hash);
int hashorpass(int passlen ,int filled );
char *Hashreturn(char *user, char *password)
{
    int seed = seedgenerator(user, password);
    srand(seed);
    char *hash = (char *)calloc(Hash_Size, sizeof(char));
    randomcharacterfill(password, hash);
    return hash;
}

// int main()
// {
//     char user[] = "A";
//     char password[] = "A";
//     char *ch=Hashreturn(user, password);
//     printf("%s",ch );

//     return 0;
// }

int seedgenerator(char *user, char *password)

{

    int user_len = strlen(user);
    int password_len = strlen(password);
    int combined_len = user_len + password_len;
    int combined_bits_user = 0;
    int comined_bits_password = 0;
    for (int i = 0; i < user_len; i++)
    {
        int bit = user[i];
        combined_bits_user += bit;
    }
    for (int i = 0; i < password_len; i++)
    {
        int bit = password[i];
        comined_bits_password += bit;
    }
    int total_combined = combined_bits_user + comined_bits_password;
    // printf("%d\t%d\t%d\t%d\t",combined_len,combined_bits_user,comined_bits_password,total_combined);

    return (total_combined * user_len);
}

int hashorpass(int passlen ,int filled)
{

    if (filled == passlen)
        return 1;
    else
    {
        return rand() % 2;
    }
}

void randomcharacterfill(char *password, char *hash)
{
    int passlength = strlen(password);

    int index = 0;
int filled = 0;
    while (index < Hash_Size-1)
    {

        if (hashorpass(passlength,filled))
        {
            int rnd_char = rand() % (allchars);
            hash[index] = avalibale[rnd_char];
        }
        else
        {
            hash[index] = password[filled];

            filled++;
        }
        index++;
    }
    hash[index] = '\0';
}