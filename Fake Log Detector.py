# Script to display logs, mark suspicious ones, and score points in real time
print("Welcome to the Fake Log Detector - April 2022 Attack Training!")
print("Read the 50 logs below and type the number of any suspicious ones.\n")

# List of fake logs (40 normal, 10 suspicious related to April 2022 attack)
logs = [
    "14:01 - User logged in: admin",                    # Normal
    "14:02 - Starting Industroyer2 simulation...",      # Suspicious: Malware start
    "14:03 - Copying file: report.txt",                 # Normal
    "14:04 - IEC-104 command sent to breaker_01",       # Suspicious: Grid control
    "14:05 - Printer status: OK",                       # Normal
    "14:06 - Deleting C:\System\eventlog.txt",          # Suspicious: Wiper action
    "14:07 - System update check",                      # Normal
    "14:08 - Network ping: 192.168.1.1",                # Normal
    "14:09 - Wipe complete - all evidence gone",        # Suspicious: Wiper finish
    "14:10 - File saved: budget.xlsx",                  # Normal
    "14:11 - User logged out: admin",                   # Normal
    "14:12 - Checking disk space",                      # Normal
    "14:13 - Email sent: status update",                # Normal
    "14:14 - Windows Defender scan started",            # Normal
    "14:15 - Battery level: 85%",                       # Normal
    "14:16 - Mouse movement detected",                  # Normal
    "14:17 - Keyboard input: typing memo",              # Normal
    "14:18 - Screen brightness adjusted",               # Normal
    "14:19 - USB device connected",                     # Normal
    "14:20 - Software update downloaded",               # Normal
    "14:21 - IEC-104 traffic spike: port 2404",         # Suspicious: Grid attack
    "14:22 - Browser opened: company site",             # Normal
    "14:23 - File opened: notes.docx",                  # Normal
    "14:24 - System idle for 2 minutes",                # Normal
    "14:25 - Erasing temporary files",                  # Suspicious: Wiper action
    "14:26 - Printer queued: 1 job",                    # Normal
    "14:27 - Audio volume: 70%",                        # Normal
    "14:28 - Wallpaper changed: beach.png",             # Normal
    "14:29 - Task manager opened",                      # Normal
    "14:30 - CPU usage: 45%",                           # Normal
    "14:31 - Network speed test: 60 Mbps",              # Normal
    "14:32 - SubstationCmd.exe executed",               # Suspicious: Malware run
    "14:33 - File archived: data.zip",                  # Normal
    "14:34 - IT-OT boundary access detected",           # Suspicious: Attack bridge
    "14:35 - Screen locked by user",                    # Normal
    "14:36 - Deleting C:\Logs\system_backup.dat",       # Suspicious: Wiper action
    "14:37 - Email received: meeting invite",           # Normal
    "14:38 - Mouse clicked: desktop icon",              # Normal
    "14:39 - Power grid status checked",                # Normal
    "14:40 - Windows event viewer opened",              # Normal
    "14:41 - File downloaded: update.exe",              # Normal
    "14:42 - Network connection stable",                # Normal
    "14:43 - Breaker_02 status: OFFLINE",               # Suspicious: Grid impact
    "14:44 - Printer offline",                          # Normal
    "14:45 - User session timeout",                     # Normal
    "14:46 - Disk cleanup started",                     # Normal
    "14:47 - Audio muted",                              # Normal
    "14:48 - Browser closed",                           # Normal
    "14:49 - System restart initiated",                 # Normal
    "14:50 - Login attempt: guest",                     # Normal
]

# Display logs with numbers
for i, log in enumerate(logs, start=1):
    print(f"{i}. {log}")

# Define correct suspicious logs (10 related to April 2022 attack)
correct_suspicious = {2, 4, 6, 9, 21, 25, 32, 34, 36, 43}  # Matches attack IoCs
max_points = 10  # Total possible correct logs

# Get user input for suspicious logs with real-time scoring
print("\nType the number of a suspicious log (e.g., '2' for line 2). Type '0' when done.")
suspicious_logs = []
points = 0

while True:
    choice = input("Enter a number (1-50, or 0 to finish): ")
    if choice == "0":
        break
    try:
        num = int(choice)
        if 1 <= num <= 50:
            if num not in suspicious_logs:  # Avoid duplicates
                suspicious_logs.append(num)
                # Update points after each entry
                if num in correct_suspicious:
                    points += 1
                    print(f"Correct! Marked log {num}: {logs[num-1]}")
                else:
                    print(f"Wrong! Marked log {num}: {logs[num-1]} (not suspicious)")
                print(f"Current score: {points}/{max_points}")
                
                # Check if all correct logs are found
                user_set = set(suspicious_logs)
                if user_set.issuperset(correct_suspicious):  # All 10 correct logs marked
                    print("\nAwesome! You've found all 10 clues from the April 2022 attack!")
                    print("You can keep going or type '0' to finish.")
            else:
                print("You already picked that one!")
        else:
            print("Please pick a number between 1 and 50!")
    except ValueError:
        print("Oops, enter a valid number!")

# Show final results
print("\nYou marked these logs as suspicious:")
for num in sorted(suspicious_logs):
    print(f"- {logs[num-1]}")

# Display final score and feedback
print(f"\nFinal score: {points}/{max_points}")
if points == max_points and len(user_set & correct_suspicious) == len(correct_suspicious):
    print("Perfect! You nailed all the clues from the April 2022 attack!")
elif user_set & correct_suspicious:  # Some correct
    print(f"Good effort! You got {len(user_set & correct_suspicious)} attack clues.")
    print("Correct ones were: 2, 4, 6, 9, 21, 25, 32, 34, 36, 43 (attack actions).")
else:
    print("No attack clues caught! Correct ones were: 2, 4, 6, 9, 21, 25, 32, 34, 36, 43.")
    print("Look for 'wipe,' 'delete,' or grid control next time!")

print("Training tip: In April 2022, Sandworm used Industroyer2 and a wiper to disrupt Ukraine’s power grid.")