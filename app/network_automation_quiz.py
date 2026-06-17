# ─────────────────────────────────────────────────────────────────────────────
# Network Automation quiz — add "ch-network-automation" to the QUIZZES dict
# in app/quizzes.py (see header there for the exact two-line wiring).
# ─────────────────────────────────────────────────────────────────────────────

NETWORK_AUTOMATION_QUIZ = {
    "ch-network-automation": {
        "title": "Network Automation Quiz: Paramiko · Netmiko · Ansible · NAPALM · Telnet",
        "questions": [
            {
                "id": "q1",
                "type": "multiple_choice",
                "question": "What does Netmiko know that Paramiko doesn't?",
                "options": [
                    "How to open a TCP socket",
                    "The device_type, so it can handle paging and config mode automatically",
                    "The device's IP address in advance",
                    "How to encrypt traffic"
                ],
                "answer": 1,
                "explanation": "Paramiko is generic SSH -- it has no idea what kind of device it's talking to. Netmiko's device_type parameter lets it handle vendor-specific quirks like --More-- paging and enable mode for you.",
            },
            {
                "id": "q2",
                "type": "multiple_choice",
                "question": "What does NAPALM's compare_config() let you do?",
                "options": [
                    "Permanently apply a config change",
                    "Preview a proposed change before committing it",
                    "Compare two different devices' hardware",
                    "Roll back the last five commits automatically"
                ],
                "answer": 1,
                "explanation": "load_merge_candidate() stages a change without applying it, and compare_config() shows you the diff so you can decide whether to commit() or discard_config() before anything goes live.",
            },
            {
                "id": "q3",
                "type": "true_false",
                "question": "An idempotent automation task should produce no additional changes if you run it a second time.",
                "answer": True,
                "explanation": "That's the definition of idempotent: running it once or a hundred times leaves the system in the same end state. It's why Ansible playbooks check before changing instead of blindly applying.",
            },
            {
                "id": "q4",
                "type": "multiple_choice",
                "question": "Why is Telnet considered unsafe for production use?",
                "options": [
                    "It's too slow for modern networks",
                    "It only works on Cisco devices",
                    "Usernames, passwords, and commands travel as plain, unencrypted text",
                    "It requires a paid license"
                ],
                "answer": 2,
                "explanation": "Telnet predates encrypted remote access. Anyone capturing the traffic -- on the wire, a mirrored port, or a compromised hop -- can read credentials and commands directly.",
            },
            {
                "id": "q5",
                "type": "multiple_choice",
                "question": "In Ansible, what does the inventory file (e.g. inventory.ini) define?",
                "options": [
                    "The exact CLI commands to run",
                    "Which devices exist and how to connect to them",
                    "The Python version required",
                    "The diff to apply to a device"
                ],
                "answer": 1,
                "explanation": "The inventory lists devices, groups, and connection details (IP, OS type, credentials). The playbook then says what to do to everything in that inventory.",
            },
            {
                "id": "q6",
                "type": "multiple_choice",
                "question": "In the 5-step automation workflow (Inventory -> Connect -> Execute -> Parse -> Act), what does 'Parse' mean?",
                "options": [
                    "Opening the SSH connection",
                    "Listing every device you own",
                    "Turning a device's raw text reply into structured data you can act on",
                    "Saving the config to disk"
                ],
                "answer": 2,
                "explanation": "A device sends back a wall of CLI text. Parsing means pulling out just the piece you need -- a version number, an open-port list -- instead of reading the whole reply by hand.",
            },
        ],
    },
}
