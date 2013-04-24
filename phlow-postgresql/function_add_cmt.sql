CREATE OR REPLACE FUNCTION cmt (varchar) RETURNS void AS $_$

BEGIN

IF EXISTS (
    SELECT *
    FROM   pg_catalog.pg_tables 
    WHERE  schemaname = 'public'
    AND    tablename = $1
    ) THEN
   RAISE NOTICE 'Table already exists!';
ELSE
   EXECUTE 'CREATE TABLE ' ||$1|| 
      ' (ip character(15) NOT NULL default '''','
      ' bytesSent bigint NOT NULL default ''0'','
      ' bytesRcvd bigint NOT NULL default ''0'','
      ' date integer NOT NULL default ''0'','
      ' PRIMARY KEY (date, ip))';
END IF;

END;
$_$
  LANGUAGE plpgsql;
