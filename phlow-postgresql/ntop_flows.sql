CREATE TABLE flows (
  ipSrc character(15) NOT NULL default '',
  ipDst character(15) NOT NULL default '',
  pktSent integer NOT NULL default '0',
  bytesSent integer NOT NULL default '0',
  startTime timestamp NOT NULL default '00:00:00',
  endTime timestamp NOT NULL default '00:00:00',
  srcPort integer NOT NULL default '0',
  dstPort integer NOT NULL default '0',
  tcpFlags smallint NOT NULL default '0',
  proto smallint NOT NULL default '0',
  tos smallint NOT NULL default '0'
);

    


