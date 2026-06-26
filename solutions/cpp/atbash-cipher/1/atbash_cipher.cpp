#include "atbash_cipher.h"

namespace atbash_cipher {
const std::string key = "abcdefghijklmnopqrstuvwxyz";
    
void convert_lowercase(std::string& plain_text){
    /*A copy of the input is made in the encode function. To avoid making another copy, we use pass by reference.*/
    for (char& c: plain_text){
        if (c >= 'A' && c <= 'Z') c += 32;
    }
}

// Encryption Function
std::string encode(std::string plain_text){
    std::string cipher_text{""};
    int count{0}; // To keep track of when to add a space 
    convert_lowercase(plain_text); // Making all characters in to lowercase
    for (char c: plain_text){
        if ((c >= 'a' && c <= 'z')){ // If c is a letter
            if (count > 0 && count % 5 == 0) cipher_text += " ";
            cipher_text += key[25 - (c - 'a')];
            count += 1;
        }
        else if (c >= '0' && c <= '9'){ //If c is a number
            if (count > 0 && count % 5 == 0) cipher_text += " ";
            cipher_text += c;
            count += 1;
        }
        else continue; // If c is a whitespace or punctutation
    }
    return cipher_text;
}

// Decryption Function
std::string decode(const std::string& cipher_text){
/*Using pass by reference as there is no need to modify the incoming ciphertext and hence no need to make a copy*/
    std::string plain_text {""};
    for (char c: cipher_text){
        if (c >= 'a' && c <= 'z') plain_text += key[25 - (c - 'a')]; // If c is a letter
        else if (c >= '0' && c <= '9') plain_text += c; //If c is a number
        else continue;                                 //If c is a whitespace
    }
    return plain_text;
}
}  // namespace atbash_cipher
