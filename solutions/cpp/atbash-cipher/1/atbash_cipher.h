#pragma once
#include <string>
namespace atbash_cipher {
void convert_lowercase(std::string& plain_text);
std::string encode(std::string plain_text);
std::string decode(const std::string& cipher_text);
}  // namespace atbash_cipher
