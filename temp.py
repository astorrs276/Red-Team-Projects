# compile the ahk scripts more efficiently
chars = [
    'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
    'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
    'z', 'x', 'c', 'v', 'b', 'n', 'm',
]
chars2 = [
    'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'q',
    's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'a',
    'x', 'c', 'v', 'b', 'n', 'm', 'z'
]
nums = [
    '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
]
nums2 = [
    '2', '3', '4', '5', '6', '7', '8', '9', '0', '1',
]
result = "#SingleInstance Force\n\n"

for i in range(len(nums)):
    result += "$" + nums[i] + '::{\n    Send "' + nums2[i] + '"\n}\n'

for i in range(len(chars)):
    result += "$" + chars[i] + '::{\n    Send "' + chars2[i] + '"\n}\n'
    result += "$+" + chars[i] + '::{\n    Send "+' + chars2[i] + '"\n}\n'

print(result + "^Esc::ExitApp")
