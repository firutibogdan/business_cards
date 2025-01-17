Table DOMAIN {
  DOMAIN_ID int [pk, increment, not null]
  DOMAIN_NAME varchar [not null, unique]
}

Table DEPARTMENT {
  DEPARTMENT_ID int [pk, increment, not null]
  DEPARTMENT_NAME varchar [not null, unique]
}

Table JOB {
  JOB_ID int [pk, increment, not null]
  JOB_NAME varchar [not null, unique]
}

Table COUNTRY {
  COUNTRY_ID int [pk, increment, not null]
  COUNTRY_NAME varchar [not null, unique]
}

Table CITY {
  CITY_ID int [pk, increment, not null]
  CITY_NAME varchar [not null, unique]
  CITY_POPULATION int
  CITY_AVAILABLE_JOBS int
  COUNTRY_ID int [ref: > COUNTRY.COUNTRY_ID]
}

Table COMPANY {
  COMPANY_ID int [pk, increment, not null]
	COMPANY_NAME VARCHAR [NOT NULL, UNIQUE]
	COMPANY_PHONE VARCHAR [NOT NULL]
	COMPANY_EMAIL VARCHAR [NOT NULL]
	COMPANY_ADDRESS VARCHAR [NOT NULL]
	DOMAIN_ID INT [ref: > DOMAIN.DOMAIN_ID]
	CITY_ID INT [ref: > CITY.CITY_ID]
	LATITUDE FLOAT [NOT NULL]
	LONGITUDE FLOAT [NOT NULL]
}

Table PERSON {
  PERSON_ID int [pk, increment, not null]
	PERSON_NAME VARCHAR [NOT NULL]
	PERSON_SURNAME VARCHAR [NOT NULL]
	PERSONAL_PHONE VARCHAR [NOT NULL]
	PERSONAL_EMAIL VARCHAR [NOT NULL, UNIQUE]
	PERSONAL_PASSWORD VARCHAR [NOT NULL]
	BIRTHDAY DATE
	COMPANY_ID INT [ref: > COMPANY.COMPANY_ID]
	DEPARTMENT_ID INT [ref: > DOMAIN.DOMAIN_ID]
	JOB_ID INT [ref: > JOB.JOB_ID]
	CITY_ID INT [ref: > CITY.CITY_ID]
}

Table LOGS {
  PERSON_NAME VARCHAR [NOT NULL]
	PERSON_SURNAME VARCHAR [NOT NULL]
	USERNAME VARCHAR [NOT NULL]
	ACTIVITY VARCHAR [NOT NULL]
	LTIME DATE [NOT NULL]
}

Table MSGS {
  MSG_ID int [pk, increment, not null]
	MSG VARCHAR [NOT NULL]
	SOURCE VARCHAR [NOT NULL]
	DESTINATION VARCHAR [NOT NULL]
	TIME_OF_MSG TIMESTAMP [NOT NULL]
}
