import sqlite3

conn = sqlite3.connect('smartbms.db')

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS User (
            UserID integer,
            RoleID integer,
            CardID integer,
            DeptID integer,
            Password text,
            LastName text,
            FirstName text,
            Email text,
            MobileNo text,
            Gender text,
            BirthDate text,
            PersonToContact text,
            EmergencyContactNo integer
)""")

c.execute("""CREATE TABLE IF NOT EXISTS Department (
            DeptID integer,
            DeptName text,
            IsEmployee integer
)""")

c.execute("""CREATE TABLE IF NOT EXISTS Card (
            CardID integer,
            IsActve integer,
            DateReg text,
            DateExp text
)""")

c.execute("""CREATE TABLE IF NOT EXISTS Facility (
            FacilityID integer,
            FacConfigID integer,
            FacilityName text,
            FacilityType text,
            IsActive integer,
            Area text,
            Remarks text
)""")

c.execute("""CREATE TABLE IF NOT EXISTS System (
            SystemID integer,
            SysConfigID integer,
            FacilityID integer,
            SystemType text,
            IsActive integer,
            Remarks text
)""")

c.execute("""CREATE TABLE IF NOT EXISTS Device (
            DeviceID integer,
            DevConfigID integer,
            SystemID text,
            DeviceType text,
            IsActive integer,
            Remarks text
)""")

c.execute("""CREATE TABLE IF NOT EXISTS AlertMessage (
            AlertMesID integer,
            AlertType text,
            AlertContent text,
            AlertAudio text,
            IsDefault integer
)""")

c.execute("""CREATE TABLE IF NOT EXISTS Event (
            EventID integer,
            DeviceID integer,
            EventType text,
            IsUserAccess integer,
            LogStartDate text,
            LogStartTime text,
            LogEndDate text,
            LogEndTime text,
            Remarks text
)""")

c.execute("""CREATE TABLE IF NOT EXISTS UserAccess (
            UserAccID integer,
            UserID integer,
            EventID integer,
            UserAccType text
)""")

c.execute("""CREATE TABLE IF NOT EXISTS AttendLog (
            AttendID integer,
            UserAccID integer,
            IsTimeIn integer
)""")

c.execute("""CREATE TABLE IF NOT EXISTS ConfigLog (
            ConfigID integer,
            UserAccID integer,
            ConfigType text
)""")

c.execute("""CREATE TABLE IF NOT EXISTS AlertLog (
            AlertID integer,
            UserAccID integer,
            AlertMesID integer,
            AlertLoudness integer,
            AlertDuration integer,
            PrioLevel1 integer,
            PrioLevel2 integer,
            PrioLevel3 integer,
            PrioLevel4 integer,
            PrioLevelEtc integer
)""")

c.execute("""CREATE TABLE IF NOT EXISTS IntercomLog (
            IntercomID integer,
            UserAccID integer,
            DeviceID integer,
            IsBroadcastAll integer,
            IsBroadcast1 integer,
            IsBroadcast2 integer,
            IsBroadcast3 integer,
            IsBroadcast4 integer,
            IsBroadcastEtc integer
)""")

c.execute("""CREATE TABLE IF NOT EXISTS ElectricalLog (
            ElectricalID integer,
            EventID integer,
            VoltageValue integer,
            CurrentValue integer
)""")

c.execute("""CREATE TABLE IF NOT EXISTS GasWaterLog (
            GasWaterID integer,
            EventID integer,
            IsWater integer,
            PressureValue text,
            FlowValue text
)""")

c.execute("""CREATE TABLE IF NOT EXISTS SensorLog (
            SensorID integer,
            EventID integer,
            SensorValue integer
)""")

c.execute("""CREATE TABLE IF NOT EXISTS AlarmLog (
            AlarmID integer,
            EventID integer,
            IsManualOff integer
)""")

c.execute("""CREATE TABLE IF NOT EXISTS CCTVLog (
            CCTVID integer,
            EventID integer
)""")

c.execute("""CREATE TABLE IF NOT EXISTS ChatHeader (
            ChatID integer,
            UserAccID integer,
            SentDate text,
            SentTime text,
            IsBroadcasted integer,
            IsDefault integer,
            IsSent integer
)""")

c.execute("""CREATE TABLE IF NOT EXISTS ChatLog (
            ChatID integer,
            ChatMesID integer,
            UserID integer,
            ChatContent text
)""")

c.execute("""CREATE TABLE IF NOT EXISTS HomeConLog (
            ContentLogID integer,
            UserAccID integer,
            ContentType text
)""")

c.execute("""CREATE TABLE IF NOT EXISTS News (
            NewsID integer,
            ContentLogID integer
)""")

c.execute("""CREATE TABLE IF NOT EXISTS BlogPost (
            PostID integer,
            ContentLogID integer
)""")

c.execute("""CREATE TABLE IF NOT EXISTS Slide (
            HomeSlideID integer,
            ContentLogID integer
)""")

c.execute("""CREATE TABLE IF NOT EXISTS UserConfig (
            RoleID integer,
            ConfigID integer
)""")

c.execute("""CREATE TABLE IF NOT EXISTS FacConfig (
            FacConfigID integer,
            ConfigID integer
)""")

c.execute("""CREATE TABLE IF NOT EXISTS SysConfig (
            SysConfigID integer,
            ConfigID integer
)""")

c.execute("""CREATE TABLE IF NOT EXISTS DevConfig (
            DevConfigID integer,
            ConfigID integer
)""")

c.execute("""CREATE TABLE IF NOT EXISTS PageConfig (
            PageConfigID integer,
            ConfigID integer
)""")

c.execute("""CREATE TABLE IF NOT EXISTS AccessConfig (
            AccConfigID integer,
            ConfigID integer
)""")

conn.commit()

conn.close()