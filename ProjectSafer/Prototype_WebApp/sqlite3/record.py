import sqlite3

conn = sqlite3.connect('smartbms.db')

c = conn.cursor()

c.execute("""INSERT INTO User VALUES (
            '201129001001',
            '201129002001',
            '201129003001',
            '201129004001',
            'Password',
            'De Tester',
            'Tester',
            'tester@gmail.com',
            '09111111111',
            'Male',
            'January 1, 2001',
            'Tester''s Father',
            '09000000000'
)""")

c.execute("""INSERT INTO Department VALUES (
            '201129004001',
            'Faculty',
            '1'
)""")

c.execute("""INSERT INTO Card VALUES (
            '201129003001',
            '1',
            'March 15, 2020',
            'March 15, 2025'
)""")

c.execute("""INSERT INTO Facility VALUES (
            '201129005001',
            '201129009001',
            'Director''s Office',
            'Office',
            '1',
            'Ground Floor',
            ''
)""")

c.execute("""INSERT INTO System VALUES (
            '201129006001',
            '201129010001',
            '201129005001',
            'Access Control',
            '1',
            ''
)""")

c.execute("""INSERT INTO Device VALUES (
            '201129007001',
            '201129011001',
            '201129006001',
            'RFID Reader',
            '1',
            ''
)""")

c.execute("""INSERT INTO AlertMessage VALUES (
            '201129014001',
            'Fire Alert',
            'Calmly and safely evacuate the building now.',
            'alert.mp3',
            'Trye'
)""")

c.execute("""INSERT INTO Event VALUES (
            '201129020001',
            '201129007001',
            'Sensor',
            '1',
            'November 1, 2020',
            '12:00',
            'November 1, 2020',
            '12:30',
            'Smoke Detected'
)""")

c.execute("""INSERT INTO UserAccess VALUES (
            '201129015001',
            '201129001001',
            '201129020001',
            'Door Access'
)""")

c.execute("""INSERT INTO AttendLog VALUES (
            '201129016001',
            '201129015001',
            '0'
)""")

c.execute("""INSERT INTO ConfigLog VALUES (
            '201129017001',
            '201129015001',
            'System Settings'
)""")

c.execute("""INSERT INTO AlertLog VALUES (
            '201129018001',
            '201129015001',
            '201129014001',
            '5',
            '30',
            '5',
            '4',
            '3',
            '2',
            '1'
)""")

c.execute("""INSERT INTO IntercomLog VALUES (
            '201129019001',
            '201129015001',
            '201129007001',
            '1',
            '0',
            '0',
            '0',
            '0',
            '0'
)""")

c.execute("""INSERT INTO ElectricalLog VALUES (
            '201129021001',
            '201129020001',
            '12',
            '100'
)""")

c.execute("""INSERT INTO GasWaterLog VALUES (
            '201129022001',
            '201129020001',
            '1',
            '100',
            '500'
)""")

c.execute("""INSERT INTO SensorLog VALUES (
            '201129023001',
            '201129020001',
            '750'
)""")

c.execute("""INSERT INTO AlarmLog VALUES(
            '201129024001',
            '201129020001',
            '0'
)""")

c.execute("""INSERT INTO CCTVLog VALUES (
            '201129025001',
            '201129020001'
)""")

c.execute("""INSERT INTO ChatHeader VALUES (
            '201129026001',
            '201129015001',
            'November 30, 2020',
            '13:00',
            '0',
            '0',
            '1'
)""")

c.execute("""INSERT INTO ChatLog VALUES (
            '201129026001',
            '201129027001',
            '201129001001',
            'Hello World!'
)""")

c.execute("""INSERT INTO HomeConLog VALUES (
            '201129028001',
            '201129015001',
            'Blog'
)""")

c.execute("""INSERT INTO News VALUES (
            '201129029001',
            '201129028001'
)""")

c.execute("""INSERT INTO BlogPost VALUES (
            '201129030001',
            '201129028001'
)""")

c.execute("""INSERT INTO Slide VALUES (
            '201129031001',
            '201129028001'
)""")

c.execute("""INSERT INTO UserConfig VALUES (
            '201129002001',
            '201129017001'
)""")

c.execute("""INSERT INTO FacConfig VALUES (
            '201129032001',
            '201129017001'
)""")

c.execute("""INSERT INTO SysConfig VALUES (
            '201129033001',
            '201129017001'
)""")

c.execute("""INSERT INTO DevConfig VALUES (
            '201129034001',
            '201129017001'
)""")

c.execute("""INSERT INTO PageConfig VALUES (
            '201129035001',
            '201129017001'
)""")

c.execute("""INSERT INTO AccessConfig VALUES (
            '201129036001',
            '201129017001'
)""")

conn.commit()

conn.close()