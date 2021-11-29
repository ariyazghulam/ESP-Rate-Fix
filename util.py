import numpy as np

length = 582
problems_arr = ['Gas', 'Mid-Low Reservoir Pressure', 'Fine Sands', 'Fishing Problem', 'Casing Damaged', 'Sand', '-', 'Tight Formation', 'Fines Migration', 'Scale', 'Sand Erosion', 'Low Reservoir Pressure', 'Hi TM', 'Low Influx', 'Corrosive']
pumps_arr = ['Q20', 'Q08', 'QM265', 'QN55', 'QM200', 'RC1000', 'DN1750', 'SN3600', 'QN70', 'Q10', 'QN120']
platforms_arr = ['AI', 'AR', 'AT', 'CI A', 'CI B', 'CI C', 'CI D', 'CI E', 'CI F', 'CI G', 'CI H', 'RA', 'FA-A', 'FA-B', 'FA-C', 'GI A', 'IND A', 'INT A', 'INT AC', 'INT B', 'KARM A', 'KART AC', 'KIT A', 'KRI A', 'KRI B', 'KRI C', 'KRI D', 'KRI E', 'LID AC', 'LI AC', 'WAN BC', 'WAN-A', 'INTA', 'INTA AC', 'NO', 'RAA A', 'RAA B', 'RAA C', 'RAA D', 'RAA E', 'RAA F', 'RAA G', 'RAA H', 'RAA I', 'ZEL AC', 'SEL A', 'SUN A', 'SUN B', 'SURA AC', 'WA-A', 'TER AC', 'TIT A', 'VTA AC', 'WDA', 'WDI A', 'WDI B', 'WDI C', 'WDI DC', 'WDI E', 'WDI F', 'WDI G', 'WDI H', 'WDI-D', 'WNDRI AC', 'YAN-A', 'YAN-AC', 'YV A', 'YVO B', 'ZEDA A', 'ZEDA B', 'ZEDA C', 'ZEDA D', 'ZEDA-E']
wells_arr = ['AI-01', 'AI-02', 'AI-03', 'AI-04', 'AI-05', 'AI-07', 'AI-09', 'AI-13', 'AI-14', 'AI-15', 'AR-C1', 'AR-C2', 'AR-C6', 'AT-C1', 'AT-C8', 'AT-CA', 'CIA-03', 'CIA-04ST', 'CIA-08', 'CIA-10ST', 'CIA-11ST', 'CIA-12', 'CIB-05', 'CIC-01', 'CIC-03', 'CIC-05S', 'CIC-06', 'CIC-07', 'CIC-10', 'CIC-11', 'CIC-12', 'CID-02', 'CID-04', 'CID-07', 'CID-10', 'CID-11ST', 'CID-12', 'CID-14', 'CID-15', 'CID-A', 'CID-B', 'CIE-01', 'CIE-03', 'CIE-09', 'CIE-11', 'CIE-12', 'CIE-13', 'CIF-01', 'CIF-05', 'CIF-08', 'CIF-11', 'CIF-12', 'CIF-14', 'CIF-15', 'CIF-A', 'CIG-03', 'CIG-08', 'CIG-12', 'CIG-13', 'CIG-14', 'CIG-15', 'CIG-A', 'CIH-01', 'CIH-04', 'CIH-06', 'CIH-A', 'CIH-B', 'ER-C10ST', 'ER-C4', 'FA-02', 'FA-02:TA', 'FA-04', 'FA-04:TA', 'FA-07', 'FA-07:TA', 'FA-14', 'FRB-01', 'FRB-02', 'FRB-07', 'FRB-08', 'FRB-10', 'FRB-10:TA', 'FRB-12', 'FRB-12:TA', 'FRB-13', 'FRB-13:TA', 'FRB-15', 'FRB-A', 'FRB-B', 'FRC-01', 'FRC-01:TA', 'FRC-10', 'FRC-11', 'FRC-11:TA', 'GI-01', 'GI-09', 'GI-10', 'GI-11', 'GI-12', 'GI-18', 'IN-02', 'IN-05', 'IN-11', 'IN-24', 'IN-25', 'ITA-04', 'ITA-05', 'ITA-08', 'ITA-16', 'ITA-18', 'ITA-C22', 'ITA-C23', 'ITB-01', 'ITB-02', 'ITB-04', 'KA-14', 'KI-07', 'KR-01', 'KR-03', 'KR-05', 'KR-06', 'KR-07', 'KR-09', 'KR-14', 'KRB-01', 'KRB-03', 'KRB-04', 'KRB-06', 'KRB-07', 'KRC-01', 'KRC-02', 'KRC-04', 'KRC-08', 'KRD-02', 'KRD-03', 'KRD-06S', 'KRD-07', 'KRD-08', 'KRD-09', 'KRD-15', 'KRD-16', 'KRE-01', 'KRE-02', 'KRE-07', 'KTA-C01', 'KTA-C03', 'KTA-C04', 'KTA-C06', 'KTA-C07', 'LIA-C02', 'LIA-C06', 'LIA-C07', 'LIA-C08', 'LIA-C03', 'LIA-C04', 'NEA-01', 'NEA-02', 'NEA-03ST', 'NEA-04ST', 'NEA-05', 'NEA-06', 'NEA-08ST', 'NEA-09ST', 'NEA-10', 'NEA-11', 'NEA-12', 'NEA-14', 'NEA-15', 'NEA-24ML', 'NEA-C17', 'NEA-C18', 'NEA-C19', 'NEA-C20', 'NEA-C21', 'NEA-C25', 'NEA-C26', 'NEA-C27ST', 'NEA-C28', 'NOA-01', 'NOA-02', 'NOA-03', 'NOA-04', 'NWA-C2S', 'NWA-C2S:TA', 'NWA-C3', 'NWA-C4', 'NWA-CAN A', 'NWA-CAN B', 'NWB-C7', 'RAA-01', 'RAA-04', 'RAA-05', 'RAA-CAN A', 'RAB-01', 'RAB-05', 'RAB-06', 'RAB-10', 'RAB-11', 'RAC-01', 'RAC-06', 'RAC-07', 'RAC-14', 'RAC-CAN', 'RAD-02', 'RAD-08', 'RAD-09', 'RAD-12', 'RAD-13', 'RAE-01', 'RAE-02', 'RAE-03', 'RAE-06', 'RAE-CAN A', 'RAF-01', 'RAF-02', 'RAF-03ST', 'RAF-06', 'RAF-08', 'RAF-11', 'RAF-13', 'RAF-14', 'RAF-15', 'RAF-17H', 'RAF-CAN', 'RAG-01', 'RAG-02', 'RAG-07', 'RAG-10', 'RAG-11', 'RAG-CAN A', 'RAH-02', 'RAH-04', 'RAH-08', 'RAH-CAN A', 'RAI-02', 'RAI-03', 'RAI-08', 'RAI-CAN A', 'SE-01', 'SE-02', 'SE-03', 'SE-09', 'SE-10', 'SU-06', 'SU-10', 'SU-11', 'SU-13', 'SUB-01', 'SUB-02', 'SUB-04', 'SUB-05', 'SUB-08', 'SUA-C01', 'SUA-C02', 'SUA-C03H', 'SUA-C04', 'SWA-C1', 'SWA-C2', 'SWA-C5', 'SWA-C5:TA', 'SWA-C8', 'SWA-C9', 'SZ-C1', 'SZ-C10', 'SZ-C11', 'SZ-C6', 'SZ-C8', 'SZ-C9', 'TE-C4', 'TE-C6', 'TE-CAN A', 'TE-CAN B', 'TI-02', 'TI-05', 'TI-15', 'VI-C01', 'VI-C02', 'VI-C03', 'VI-C04', 'VI-CAN A', 'VI-CAN B', 'WA-01', 'WA-02', 'WA-03', 'WA-06', 'WA-09', 'WA-10', 'WA-11', 'WA-12', 'WI-01', 'WI-02S', 'WI-03', 'WI-04', 'WI-05', 'WI-07', 'WI-08', 'WI-09', 'WI-10', 'WI-11', 'WI-14', 'WI-15', 'WI-16', 'WI-18S', 'WI-19', 'WI-20', 'WI-22', 'WI-24', 'WI-25', 'WI-26', 'WI-27', 'WI-28', 'WI-32', 'WI-35', 'WI-36ST', 'WI-37', 'WI-39', 'WI-CAN A', 'WI-CAN B', 'WIB-01', 'WIB-02ST', 'WIB-04', 'WIB-07', 'WIB-08', 'WIB-10', 'WIB-15', 'WIB-16', 'WIB-17', 'WIB-18', 'WIB-22', 'WIB-23', 'WIB-24', 'WIB-25', 'WIB-29', 'WIB-31', 'WIB-32', 'WIB-33', 'WIB-34', 'WIB-35', 'WIB-36', 'WIB-CAN A', 'WIB-CAN B', 'WIC-03', 'WIC-04', 'WIC-05', 'WIC-06', 'WIC-07', 'WIC-08', 'WIC-09', 'WIC-12', 'WIC-13', 'WIC-16', 'WIC-17', 'WIC-18', 'WIC-19', 'WIC-22', 'WIC-25', 'WIC-30', 'WIC-31', 'WIC-32', 'WIC-33', 'WIC-34', 'WIC-35', 'WIC-36', 'WIC-37', 'WIC-39', 'WIC-41', 'WIC-CAN A', 'WIC-CAN B', 'WID-01', 'WID-02', 'WID-03', 'WID-04', 'WID-05', 'WID-07', 'WID-08ST', 'WID-09', 'WID-09:TA', 'WID-11', 'WID-12', 'WID-15', 'WID-16', 'WID-20', 'WID-21', 'WID-22', 'WID-23', 'WID-25', 'WID-26', 'WID-28', 'WID-29', 'WID-31', 'WID-44', 'WID-48', 'WID-C17', 'WID-C38', 'WID-C41', 'WID-C42', 'WDD-CA34', 'WID-CAN A', 'WID-CAN B', 'WIE-02', 'WIE-03', 'WIE-04', 'WIE-08', 'WIE-10', 'WIE-11', 'WIE-12', 'WIE-13', 'WIE-14', 'WIE-16', 'WIE-19', 'WIE-20', 'WIF-01', 'WIF-07', 'WIG-01', 'WIG-03', 'WIG-05', 'WIG-06', 'WIG-08', 'WIG-09', 'WIH-04', 'WIH-07', 'WIH-08', 'WIH-10', 'WIH-11', 'WIH-12', 'WIH-13', 'WIH-15', 'WIH-16', 'WIA-C06', 'WIA-C12', 'WIA-C13', 'WIA-C15S', 'WIA-C17ST', 'WIA-C19', 'WIA-C2', 'WIA-C20', 'WIA-C21', 'WIA-C22', 'WIA-CAN A', 'WIA-CAN B', 'YA-C01', 'YA-C06', 'YA-C08', 'YA-C09', 'YA-C11', 'YA-C11:BW', 'YA-C12', 'YV-05', 'YV-06', 'YV-10', 'YV-12', 'YV-CAN A', 'YVB-03', 'YVB-04', 'YVB-08', 'YVB-10', 'YVB-14', 'YVB-15', 'ZEA-02', 'ZEA-06', 'ZEA-08', 'ZEA-CAN A', 'ZEB-01', 'ZEB-04', 'ZEB-07', 'ZEB-08', 'ZEC-09', 'ZEC-13', 'ZEC-14', 'ZED-01', 'ZED-05', 'ZED-11', 'ZED-12', 'ZEE-02', 'ZEE-06', 'ZEE-07', 'ZEE-07:TA', 'ZEE-10', 'ZEE-11']
vendors_arr = ['Vendor_Powerlift', 'Vendor_Reda']

def get_pumps(desired_q):
    pumps = []
    if desired_q >= 200 and desired_q <= 1350:
        pumps.append('RC1000')
    if desired_q >= 400 and desired_q <= 1050:
        pumps.append('Q08')
    if desired_q >= 600 and desired_q <= 1250:
        pumps.append('Q10')
    if desired_q >= 1150 and desired_q <= 2050:
        pumps.append('Q20')
    if desired_q >= 1200 and desired_q <= 2050:
        pumps.append('DN1750')
    if desired_q >= 2250 and desired_q <= 5200:
        pumps.append('QN55')
    if desired_q >= 2400 and desired_q <= 4600:
        pumps.append('SN3600')
    if desired_q >= 3400 and desired_q <= 7900:
        pumps.append('QN70')
    if desired_q >= 6000 and desired_q <= 12800:
        pumps.append('QN120')
    if desired_q >= 12250 and desired_q <= 18000:
        pumps.append('QM200')
    if desired_q >= 14000 and desired_q <= 24000:
        pumps.append('QM265')
    return pumps

def get_model_input(desired_q, problems, pump_type, platform, well, vendor):
    data = np.zeros(length)
    data[0] = desired_q

    # initialize index
    i = 1

    # flag problems
    for pr in problems_arr:
        if pr in problems:
            data[i] = 1
        i += 1
    
    # flag pumps
    for pu in pumps_arr:
        if pu == pump_type:
            data[i] = 1
        i += 1

    # flag platforms
    for pl in platforms_arr:
        if pl == platform:
            data[i] = 1
        i += 1

    # flag wells
    for w in wells_arr:
        if w == well:
            data[i] = 1
        i += 1

    # flag vendor
    for v in vendors_arr:
        if v == vendor:
            data[i] = 1
        i += 1
    
    assert i == length - 1
    return data

def get_model_input_arr(desired_q, problems, pumps, platform, well, vendor):
    data = []
    for pump in pumps:
        temp = get_model_input(desired_q, problems, pump, platform, well, vendor)
        data.append(temp)
    return data
