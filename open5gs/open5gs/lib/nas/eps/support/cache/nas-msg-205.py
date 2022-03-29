ies = []
ies.append({ "iei" : "", "value" : "ESM cause", "type" : "ESM cause", "reference" : "9.9.4.4", "presence" : "M", "format" : "V", "length" : "1"})
ies.append({ "iei" : "27", "value" : "Protocol configuration options", "type" : "Protocol configuration options", "reference" : "9.9.4.11", "presence" : "O", "format" : "TLV", "length" : "3-253"})
ies.append({ "iei" : "37", "value" : "T3396 value", "type" : "GPRS timer 3", "reference" : "9.9.3.16B", "presence" : "O", "format" : "TLV", "length" : "3"})
ies.append({ "iei" : "C-", "value" : "WLAN offload indication", "type" : "WLAN offload acceptability", "reference" : "9.9.4.18", "presence" : "O", "format" : "TV", "length" : "1"})
ies.append({ "iei" : "33", "value" : "NBIFOM container", "type" : "NBIFOM container", "reference" : "9.9.4.19", "presence" : "O", "format" : "TLV", "length" : "3-257"})
ies.append({ "iei" : "7B", "value" : "Extended protocol configuration options", "type" : "Extended protocol configuration options", "reference" : "9.9.4.26", "presence" : "O", "format" : "TLV-E", "length" : "4-65538"})
msg_list[key]["ies"] = ies
