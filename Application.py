from Channel import Channel

thread1 = Channel(1, "Thread 1", ["lck1", "iddqdow", "dansgaming"])
thread2 = Channel(1, "Thread 2", ["cohhcarnage", "sherriffeli"])
thread3 = Channel(1, "Thread 3", ["epicenter_en2", "summit1g", "giantwaffle"])
thread4 = Channel(1, "Thread 4", ["imaqtpie", "drdisrespectlive", "a_seagull"])

thread1.start()
thread2.start()
thread3.start()
thread4.start()