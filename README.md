# CodeAlpha-Secure-Coding-Review
Preforming static code analysis using pylint on python code. In this case basic_network_sniffer_updated.py code.
The code attached is clean code with a score of 10/10
To get clean code I used plint for static code analysis.
Pylint is a static code analysis tool for Python that helps identify errors, enforce coding standards, and improve code quality. 
It adheres to the PEP8 style guide and assigns a score to your code based on its quality.
The image below shows the installation process of pylint using command prompt.

<img width="1141" height="592" alt="Screenshot SA 1" src="https://github.com/user-attachments/assets/64e17339-bfc4-4386-978f-6960bf469a5d" />

I used a code already running without errors on both command prompt and IDLE.
The code I used with pylint is the final updated code from my first repo; Basic network sniffer.
The code was working correctly and even could perform tracert on a domain without errors.
I thought the code would pass the pylint analysis but the code failed misserably.
The image belows shows the score. The code with this misserable score is available in my first repo.
The code attached to this repo (basic_network_sniffer_updated.py code) is clean code with a 10/10 score.

<img width="1177" height="399" alt="Screenshot SA 2" src="https://github.com/user-attachments/assets/dce0a770-8de6-47d6-b701-71e185391f1a" />

The image below show the remaining errors after fixing the trailing white space error. The score improves;

<img width="1174" height="386" alt="Screenshot SA 3" src="https://github.com/user-attachments/assets/1e2d6297-e4f2-4a60-bdf5-2a071d1ce6d1" />
The image below shows the remaining errors after fixing the first indention error.
<img width="1178" height="377" alt="Screenshot SA 4" src="https://github.com/user-attachments/assets/2db0a6cc-4eeb-45c0-9824-493e5c419d2a" />
The image below shows the remaining errors after fixing the other indention errors.
<img width="1176" height="336" alt="Screenshot SA 5" src="https://github.com/user-attachments/assets/d62e4915-06a8-4f5d-ab49-645ce1e5aed5" />
The image below shows the remaining errors after fixing the trailing errors (whitespace and new lines errors)
<img width="1183" height="303" alt="Screenshot SA 6" src="https://github.com/user-attachments/assets/43214c30-0a2b-4e29-912b-e3da8ec7aad8" />
The image below shows the remaining errors after fixing the missing-module-docstring error.
<img width="1177" height="284" alt="Screenshot SA 7" src="https://github.com/user-attachments/assets/c10ea87b-59b3-4523-af4c-04ddbc1eb0bc" />
The image below shows the remaining errors and score after fixing the invalid name error.
<img width="988" height="275" alt="Screenshot SA 8" src="https://github.com/user-attachments/assets/5473972c-6855-48b8-80fd-f494f4eba349" />
The image below shows the remaining errors and score after fixing the no-name-in-module errors.
<img width="1043" height="246" alt="Screenshot SA 9" src="https://github.com/user-attachments/assets/b203069c-c322-41f8-a8ea-361dcc82e8c5" />
The image below shows the remaining errors and score after fixing the first missing-function-docstring error.
<img width="1122" height="227" alt="Screenshot SA 10" src="https://github.com/user-attachments/assets/426e5db6-4f12-409d-8e1c-4c9e999cb305" />
The image below shows the remaining errors and score after fixing the next four missing-function-docstring errors.
<img width="918" height="169" alt="Screenshot SA 11" src="https://github.com/user-attachments/assets/0f6b6fc0-1779-4393-b3f8-6813f0be80e1" />
The image below shows the remaining errors and score after fixing the function-redifined errors.
<img width="912" height="97" alt="Screenshot SA 12" src="https://github.com/user-attachments/assets/b84aab7e-480a-40bc-ae8b-7cf00568fdce" />
The image below shows the clean code after fixing the last missing-function-docstring error

<img width="613" height="65" alt="Screenshot SA clean code" src="https://github.com/user-attachments/assets/e385b2e9-433a-4c1a-b9cf-031caf79f540" />

According to pylint the static code analysis has completed with a perfect score of 10/10.

Personally I know the code, though clean, is not yet secure since I introduced an input interface for tracert which has no input validation. So a manual inspection is neccessary even after a perfect score (10/10). To be sure my code is not only clean but also secure, I will pass my clean code through a copilot test to test for vulnerabilities. Offcourse I know I have one vulnerability as a result of lack of input validation even before the test.

I carried out the copilot test and copilot came up with several security consideration based on my clean code.

The following are security the considerations by copilot:
1. Privilege Requirement: sniff() uses raw sockets which typically require root/administrator privileges. Running this with elevated rights can be risky if the environment is not well controlled.
   
2. Open Sniffing: If you deploy this on a shared network or device without user consent, it can become legally and ethically problematic—especially in corporate or public settings.

3. No Output Filtering or Sanitization: Your print statements directly output data from packets. If this were piped into a log or UI in a real system, you'd want to sanitize inputs to prevent injection attacks or unexpected code execution.

4. No Exception Handling: If a malformed packet or unsupported protocol slips through, it could throw an error. Adding basic try...except blocks would boost resilience.

5. No Rate Limiting or Control: Continuous sniffing could overwhelm your system or generate massive logs if used at scale. Always consider limiting packet capture scope or add pause intervals if needed.

Security and stabilty considerations for the tracert function:

1. Input Validation: You're using raw input() for domain entry. If someone inputs malformed or malicious data, you might hit unexpected behavior. Consider validating the domain with a regex or using libraries like socket.gethostbyname() to test DNS resolution first.

2. Privilege Requirements: ICMP packets often need elevated privileges (root/admin) to send. Running this as a regular user may fail silently or raise a PermissionError, depending on the OS.

3. Error Handling: No try-except block means if sr1() throws an exception (e.g., DNS resolution fails, ICMP unreachable), your script will crash. Wrap those calls to guard against abrupt failures.

4. Silent Failures: If a hop is firewalled or blocks ICMP, the timeout message is helpful, but you might want to add logging to track unreachable hops in a structured format.

Just show that I considered the security and stabilty considerations in my More_secure code which is a branch in this repo and ready be merged to the main code. The following images show the results of the More_secure code.

<img width="644" height="316" alt="Screenshot secure 1" src="https://github.com/user-attachments/assets/ef74f3f4-5e82-4f01-b3e4-6519fb9189a2" />

when a non existant domain is added

<img width="646" height="62" alt="Screenshot secure 2" src="https://github.com/user-attachments/assets/df695907-afd0-4503-808e-2b5f5d557b48" />

Without silent failures

<img width="651" height="88" alt="Screenshot secure 3" src="https://github.com/user-attachments/assets/dd784c42-fae9-4f90-aa62-b521da579057" />




The final secure code improved by copilot with input validation is in the Branch More_secure

When writing code you should always practice:
1. Input validation - sanitize and validate user input
2. Use least privilege principle
3. Avoid hardcoding credentials
4. Handle errors gracefully
5. Keep dependacies updated - libraries and frameworks



