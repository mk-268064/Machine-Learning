0.9::high_risk(O) :- origin_country(O, 'China').
0.7::high_risk(O) :- origin_country(O, 'Vietnam').
0.5::high_risk(O) :- high_value(O), high_risk_origin(O).

0.8::shipment_risk(O) :- high_risk(O), high_value(O).
0.3::shipment_risk(O) :- is_large_shipment(O).

query(shipment_risk(O)).
