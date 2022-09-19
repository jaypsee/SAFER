import sqlite3

conn = sqlite3.connect('smartbms.db')

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS User (
            UserID integer PRIMARY KEY,
            RoleID integer NOT NULL,
            CardID integer NOT NULL,
            DeptID integer NOT NULL,
            Password text NOT NULL,
            LastName text NOT NULL,
            FirstName text NOT NULL,
            Email text NOT NULL,
            MobileNo text NOT NULL,
            Gender text NOT NULL,
            BirthDate text NOT NULL,
            PersonToContact text NOT NULL,
            EmergencyContactNo integer NOT NULL,
            FOREIGN KEY (RoleID) REFERENCES UserConfig (RoleID),
            FOREIGN KEY (CardID) REFERENCES Card (CardID),
            FOREIGN KEY (DeptID) REFERENCES Department (DeptID)
)""")

c.execute("""CREATE TABLE IF NOT EXISTS Department (
            DeptID integer PRIMARY KEY,
            DeptName text NOT NULL,
            IsEmployee integer NOT NULL
)""")

c.execute("""CREATE TABLE IF NOT EXISTS Card (
            CardID integer PRIMARY KEY,
            IsActve integer NOT NULL,
            DateReg text NOT NULL,
            DateExp text NOT NULL
)""")

c.execute("""CREATE TABLE IF NOT EXISTS Facility (
            FacilityID integer PRIMARY KEY,
            FacConfigID integer NOT NULL,
            FacilityName text NOT NULL,
            FacilityType text NOT NULL,
            IsActive integer NOT NULL,
            Area text NOT NULL,
            Remarks text,
            FOREIGN KEY (FacConfigID) REFERENCES ConfigLog (FacConfigID)
)""")

c.execute("""CREATE TABLE IF NOT EXISTS System (
            SystemID integer PRIMARY KEY,
            SysConfigID integer NOT NULL,
            FacilityID integer NOT NULL,
            SystemType text NOT NULL,
            IsActive integer NOT NULL,
            Remarks text,
            FOREIGN KEY (SysConfigID) REFERENCES ConfigLog (SysConfigID),
            FOREIGN KEY (FacilityID) REFERENCES Facility (FacilityID)
            
)""")

c.execute("""CREATE TABLE IF NOT EXISTS Device (
            DeviceID integer PRIMARY KEY,
            DevConfigID integer NOT NULL,
            SystemID text NOT NULL,
            DeviceType text NOT NULL,
            IsActive integer NOT NULL,
            Remarks text,
            FOREIGN KEY (DevConfigID) REFERENCES ConfigLog (DevConfigID),
            FOREIGN KEY (SystemID) REFERENCES System (SystemID)
)""")

c.execute("""CREATE TABLE IF NOT EXISTS AlertMessage (
            AlertMesID integer PRIMARY KEY,
            AlertType text NOT NULL,
            AlertContent text NOT NULL,
            AlertAudio text NOT NULL,
            IsDefault integer NOT NULL
)""")

c.execute("""CREATE TABLE IF NOT EXISTS Event (
            EventID integer PRIMARY KEY,
            DeviceID integer NOT NULL,
            EventType text NOT NULL,
            IsUserAccess integer NOT NULL,
            LogStartDate text NOT NULL,
            LogStartTime text NOT NULL,
            LogEndDate text NOT NULL,
            LogEndTime text NOT NULL,
            Remarks text NOT NULL,
            FOREIGN KEY (DeviceID) REFERENCES Device (DeviceID)
)""")

c.execute("""CREATE TABLE IF NOT EXISTS UserAccess (
            UserAccID integer PRIMARY KEY,
            UserID integer NOT NULL,
            EventID integer NOT NULL,
            UserAccType text NOT NULL,
            FOREIGN KEY (EventID) REFERENCES Event (EventID),
            FOREIGN KEY (UserID) REFERENCES User (UserID)
)""")

c.execute("""CREATE TABLE IF NOT EXISTS AttendLog (
            AttendID integer PRIMARY KEY,
            UserAccID integer NOT NULL,
            IsTimeIn integer NOT NULL,
            FOREIGN KEY (UserAccID) REFERENCES UserAccess (UserAccID)
)""")

c.execute("""CREATE TABLE IF NOT EXISTS ConfigLog (
            ConfigID integer PRIMARY KEY,
            UserAccID integer NOT NULL,
            ConfigType text NOT NULL,
            FOREIGN KEY (UserAccID) REFERENCES UserAccess (UserAccID)
)""")

c.execute("""CREATE TABLE IF NOT EXISTS AlertLog (
            AlertID integer PRIMARY KEY,
            UserAccID integer NOT NULL,
            AlertMesID integer NOT NULL,
            AlertLoudness integer NOT NULL,
            AlertDuration integer NOT NULL,
            PrioLevel1 integer NOT NULL,
            PrioLevel2 integer NOT NULL,
            PrioLevel3 integer NOT NULL,
            PrioLevel4 integer NOT NULL,
            PrioLevelEtc integer NOT NULL,
            FOREIGN KEY (UserAccID) REFERENCES UserAccess (UserAccID),
            FOREIGN KEY (AlertMesID) REFERENCES AlertMessage (AlertMesID)
)""")

c.execute("""CREATE TABLE IF NOT EXISTS IntercomLog (
            IntercomID integer PRIMARY KEY,
            UserAccID integer NOT NULL,
            DeviceID integer NOT NULL,
            IsBroadcastAll integer NOT NULL,
            IsBroadcast1 integer NOT NULL,
            IsBroadcast2 integer NOT NULL,
            IsBroadcast3 integer NOT NULL,
            IsBroadcast4 integer NOT NULL,
            IsBroadcastEtc integer NOT NULL,
            FOREIGN KEY (UserAccID) REFERENCES UserAccess (UserAccID)
)""")

c.execute("""CREATE TABLE IF NOT EXISTS ElectricalLog (
            ElectricalID integer PRIMARY KEY,
            EventID integer NOT NULL,
            VoltageValue integer NOT NULL,
            CurrentValue integer NOT NULL,
            FOREIGN KEY (EventID) REFERENCES Event (EventID)
)""")

c.execute("""CREATE TABLE IF NOT EXISTS GasWaterLog (
            GasWaterID integer PRIMARY KEY,
            EventID integer NOT NULL,
            IsWater integer NOT NULL,
            PressureValue text NOT NULL,
            FlowValue text NOT NULL,
            FOREIGN KEY (EventID) REFERENCES Event (EventID)
)""")

c.execute("""CREATE TABLE IF NOT EXISTS SensorLog (
            SensorID integer PRIMARY KEY,
            EventID integer NOT NULL,
            SensorValue integer NOT NULL,
            FOREIGN KEY (EventID) REFERENCES Event (EventID)
)""")

c.execute("""CREATE TABLE IF NOT EXISTS AlarmLog (
            AlarmID integer PRIMARY KEY,
            EventID integer NOT NULL,
            IsManualOff integer NOT NULL,
            FOREIGN KEY (EventID) REFERENCES Event (EventID)
)""")

c.execute("""CREATE TABLE IF NOT EXISTS CCTVLog (
            CCTVID integer PRIMARY KEY,
            EventID integer NOT NULL,
            FOREIGN KEY (EventID) REFERENCES Event (EventID)
)""")

c.execute("""CREATE TABLE IF NOT EXISTS ChatHeader (
            ChatID integer PRIMARY KEY,
            UserAccID integer NOT NULL,
            SentDate text NOT NULL,
            SentTime text NOT NULL,
            IsBroadcasted integer NOT NULL,
            IsDefault integer NOT NULL,
            IsSent integer NOT NULL,
            FOREIGN KEY (UserAccID) REFERENCES UserAccess (UserAccID)
)""")

c.execute("""CREATE TABLE IF NOT EXISTS ChatLog (
            ChatID integer PRIMARY KEY,
            ChatMesID integer NOT NULL,
            UserID integer NOT NULL,
            ChatContent text NOT NULL,
            FOREIGN KEY (ChatID) REFERENCES ChatHeader (ChatID)
)""")

c.execute("""CREATE TABLE IF NOT EXISTS HomeConLog (
            ContentLogID integer PRIMARY KEY,
            UserAccID integer NOT NULL,
            ContentType text NOT NULL,
            FOREIGN KEY (UserAccID) REFERENCES UserAccess (UserAccID)
)""")

c.execute("""CREATE TABLE IF NOT EXISTS News (
            NewsID integer PRIMARY KEY,
            ContentLogID integer NOT NULL,
            FOREIGN KEY (ContentLogID) REFERENCES HomeConLog (ContentLogID)
)""")

c.execute("""CREATE TABLE IF NOT EXISTS BlogPost (
            PostID integer PRIMARY KEY,
            ContentLogID integer NOT NULL,
            FOREIGN KEY (ContentLogID) REFERENCES HomeConLog (ContentLogID)
)""")

c.execute("""CREATE TABLE IF NOT EXISTS Slide (
            HomeSlideID integer PRIMARY KEY,
            ContentLogID integer NOT NULL,
            FOREIGN KEY (ContentLogID) REFERENCES HomeConLog (ContentLogID)
)""")

c.execute("""CREATE TABLE IF NOT EXISTS UserConfig (
            RoleID integer PRIMARY KEY,
            ConfigID integer NOT NULL,
            FOREIGN KEY (ConfigID) REFERENCES ConfigLog (ConfigID)
)""")

c.execute("""CREATE TABLE IF NOT EXISTS FacConfig (
            FacConfigID integer PRIMARY KEY,
            ConfigID integer NOT NULL,
            FOREIGN KEY (ConfigID) REFERENCES ConfigLog (ConfigID)
)""")

c.execute("""CREATE TABLE IF NOT EXISTS SysConfig (
            SysConfigID integer PRIMARY KEY,
            ConfigID integer NOT NULL,
            FOREIGN KEY (ConfigID) REFERENCES ConfigLog (ConfigID)
)""")

c.execute("""CREATE TABLE IF NOT EXISTS DevConfig (
            DevConfigID integer PRIMARY KEY,
            ConfigID integer NOT NULL,
            FOREIGN KEY (ConfigID) REFERENCES ConfigLog (ConfigID)
)""")

c.execute("""CREATE TABLE IF NOT EXISTS PageConfig (
            PageConfigID integer PRIMARY KEY,
            ConfigID integer NOT NULL,
            FOREIGN KEY (ConfigID) REFERENCES ConfigLog (ConfigID)
)""")

c.execute("""CREATE TABLE IF NOT EXISTS AccessConfig (
            AccConfigID integer PRIMARY KEY,
            ConfigID integer NOT NULL,
            FOREIGN KEY (ConfigID) REFERENCES ConfigLog (ConfigID)
)""")

conn.commit()

conn.close()