#include "rotational_cipher.h"
#include <string>

namespace rotational_cipher {
// Encryption
std::string rotate(const std::string& plain_text, int key_shift){
    std::string cipher_text {""};
    for (char c: plain_text){
        if(c >= 'a' && c <= 'z') cipher_text += static_cast<char>('a'+(c - 'a' + key_shift) % 26);
        else if(c >= 'A' && c <= 'Z') cipher_text += static_cast<char>('A'+(c - 'A' + key_shift) % 26);
        else cipher_text += c;
    }
    return cipher_text;
}
}  // namespace rotational_cipher
