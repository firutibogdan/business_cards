TYPE=TRIGGERS
triggers='CREATE DEFINER=`root`@`localhost` TRIGGER ADD_LOG_NEW_PERSON\n    AFTER INSERT ON PERSON\n    FOR EACH ROW \nBEGIN\n	\n    INSERT INTO LOGS (PERSON_NAME, PERSON_SURNAME, USERNAME, ACTIVITY, LTIME)\n	VALUES (NEW.PERSON_NAME, NEW.PERSON_SURNAME, NEW.PERSONAL_EMAIL, \'Created new account.\', NOW());\nEND' 'CREATE DEFINER=`root`@`localhost` TRIGGER ADD_LOG_DEL_PERSON\n    BEFORE DELETE ON PERSON\n    FOR EACH ROW \nBEGIN\n\n    INSERT INTO LOGS (PERSON_NAME, PERSON_SURNAME, USERNAME, ACTIVITY, LTIME)\n	VALUES (OLD.PERSON_NAME, OLD.PERSON_SURNAME, OLD.PERSONAL_EMAIL, \'Deleted account.\', NOW());\nEND'
sql_modes=1436549152 1436549152
definers='root@localhost' 'root@localhost'
client_cs_names='latin1' 'latin1'
connection_cl_names='latin1_swedish_ci' 'latin1_swedish_ci'
db_cl_names='latin1_swedish_ci' 'latin1_swedish_ci'
created=158334235734 158334235741
