_MSG_TELEGRAM = """<DAQPRJ>
        <ANALOG>
            <CHANNEL id='0' name='ZK' dop='0'/>
            <CHANNEL id='1' name='O2' unit='%'/>
            <CHANNEL id='2' name='O2_soll' unit='%'/>
            <CHANNEL id='3' name='TK' unit='°C'/>
            <CHANNEL id='4' name='TKsoll' unit='°C' dop='0'/>
            <CHANNEL id='5' name='TRL' unit='°C'/>
            <CHANNEL id='6' name='TRLsoll' unit='°C'/>
            <CHANNEL id='7' name='TRG' unit='°C'/>
            <CHANNEL id='8' name='Leistung' unit='%' dop='0'/>
            <CHANNEL id='9' name='SZist' unit='%' dop='0'/>
            <CHANNEL id='10' name='SZsoll' unit='%'/>
            <CHANNEL id='11' name='TPo' unit='°C'/>
            <CHANNEL id='12' name='TPm' unit='°C'/>
            <CHANNEL id='13' name='TPu' unit='°C'/>
            <CHANNEL id='14' name='Spreizung' unit='°C'/>
            <CHANNEL id='15' name='RLP/PuffPumpe' unit='%' dop='0'/>
            <CHANNEL id='16' name='PufLad' unit='%'/>
            <CHANNEL id='17' name='Störungs Nr' dop='0'/>
            <CHANNEL id='18' name='Programm' dop='0'/>
            <CHANNEL id='19' name='Prim.soll' unit='%' dop='0'/>
            <CHANNEL id='20' name='Prim.ist' unit='%' dop='0'/>
            <CHANNEL id='21' name='Sek.soll' unit='%' dop='0'/>
            <CHANNEL id='22' name='Sek.ist' unit='%' dop='0'/>
            <CHANNEL id='23' name='Heiz P Lambda' unit='W' dop='2'/>
            <CHANNEL id='24' name='Heiz U Lambda' unit='V' dop='2'/>
            <CHANNEL id='25' name='Heiz I Lambda' unit='mA' dop='0'/>
            <CHANNEL id='26' name='Sens U Lambda' unit='mV'/>
            <CHANNEL id='27' name='Tplat' unit='°C' dop='0'/>
            <CHANNEL id='28' name='TVG' unit='°C'/>
            <CHANNEL id='29' name='TVG2' unit='°C'/>
            <CHANNEL id='30' name='Taus' unit='°C'/>
            <CHANNEL id='31' name='TA Gem.' unit='°C'/>
            <CHANNEL id='32' name='Max Anf Kessel' unit='°C' dop='0'/>
            <CHANNEL id='33' name='Max Anf ZenPuf' unit='°C' dop='0'/>
            <CHANNEL id='34' name='min.Leist.TRG' unit='%'/>
            <CHANNEL id='35' name='max.Leist.TRG' unit='%'/>
            <CHANNEL id='36' name='TFW' unit='°C'/>
            <CHANNEL id='37' name='FW-Anforderung' unit='°C' dop='0'/>
            <CHANNEL id='38' name='Puffer_soll oben' unit='°C' dop='0'/>
            <CHANNEL id='39' name='Puffer_soll unten' unit='°C' dop='0'/>
            <CHANNEL id='40' name='PufZustand' dop='0'/>
            <CHANNEL id='41' name='ExtHK Solltmp.' unit='°C' dop='0'/>
            <CHANNEL id='42' name='TVL_A' unit='°C'/>
            <CHANNEL id='43' name='TVLs_A' unit='°C' dop='0'/>
            <CHANNEL id='44' name='TRA_A' unit='°C'/>
            <CHANNEL id='45' name='TRs_A' unit='°C'/>
            <CHANNEL id='46' name='HKZustand_A' dop='0'/>
            <CHANNEL id='47' name='FRA Zustand' dop='0'/>
            <CHANNEL id='48' name='TVL_1' unit='°C'/>
            <CHANNEL id='49' name='TVLs_1' unit='°C' dop='0'/>
            <CHANNEL id='50' name='TRA_1' unit='°C'/>
            <CHANNEL id='51' name='TRs_1' unit='°C'/>
            <CHANNEL id='52' name='HKZustand_1' dop='0'/>
            <CHANNEL id='53' name='FR1 Zustand' dop='0'/>
            <CHANNEL id='54' name='TVL_2' unit='°C'/>
            <CHANNEL id='55' name='TVLs_2' unit='°C' dop='0'/>
            <CHANNEL id='56' name='TRA_2' unit='°C'/>
            <CHANNEL id='57' name='TRs_2' unit='°C'/>
            <CHANNEL id='58' name='HKZustand_2' dop='0'/>
            <CHANNEL id='59' name='FR2 Zustand' dop='0'/>
            <CHANNEL id='60' name='TVL_B' unit='°C'/>
            <CHANNEL id='61' name='TVLs_B' unit='°C' dop='0'/>
            <CHANNEL id='62' name='TRA_B' unit='°C'/>
            <CHANNEL id='63' name='TRs_B' unit='°C'/>
            <CHANNEL id='64' name='HKZustand_B' dop='0'/>
            <CHANNEL id='65' name='FRB Zustand' dop='0'/>
            <CHANNEL id='66' name='TBA' unit='°C'/>
            <CHANNEL id='67' name='TBs_A' unit='°C' dop='0'/>
            <CHANNEL id='68' name='TB1' unit='°C'/>
            <CHANNEL id='69' name='TBs_1' unit='°C' dop='0'/>
            <CHANNEL id='70' name='BoiZustand_1' dop='0'/>
            <CHANNEL id='71' name='TBB' unit='°C'/>
            <CHANNEL id='72' name='TBs_B' unit='°C' dop='0'/>
            <CHANNEL id='73' name='PK_ZK' dop='0'/>
            <CHANNEL id='74' name='PK_O2' unit='%'/>
            <CHANNEL id='75' name='PK_O2soll' unit='%'/>
            <CHANNEL id='76' name='PK_TK' unit='°C'/>
            <CHANNEL id='77' name='PK_TKsoll' unit='°C' dop='0'/>
            <CHANNEL id='78' name='PK_TRL' unit='°C' dop='0'/>
            <CHANNEL id='79' name='PK_TRLsoll' unit='°C' dop='0'/>
            <CHANNEL id='80' name='PK_Spreizung' unit='°C' dop='0'/>
            <CHANNEL id='81' name='PK_TRG' unit='°C' dop='0'/>
            <CHANNEL id='82' name='PK_SZ' unit='%' dop='0'/>
            <CHANNEL id='83' name='PK_SZs' unit='%' dop='0'/>
            <CHANNEL id='84' name='PK_Leistung' unit='%' dop='0'/>
            <CHANNEL id='85' name='PK_ESsoll' unit='%' dop='0'/>
            <CHANNEL id='86' name='PK_min.Leist.TRG' unit='%'/>
            <CHANNEL id='87' name='PK_max.Leist.TRG' unit='%'/>
            <CHANNEL id='88' name='max.Leist.Fuell' unit='%'/>
            <CHANNEL id='89' name='max.Leist.TPO' unit='%'/>
            <CHANNEL id='90' name='PK_ESRegler' unit='%' dop='0'/>
            <CHANNEL id='91' name='PK_KeBrstScale' unit='%' dop='0'/>
            <CHANNEL id='92' name='PK_Programm' dop='0'/>
            <CHANNEL id='93' name='PK_RLP' unit='%' dop='0'/>
            <CHANNEL id='94' name='PK_Tplat' unit='°C' dop='0'/>
            <CHANNEL id='95' name='PK_I Es' unit='mA' dop='0'/>
            <CHANNEL id='96' name='PK_I Ra' unit='mA' dop='0'/>
            <CHANNEL id='97' name='PK_I Aa' unit='mA' dop='0'/>
            <CHANNEL id='98' name='PK_I Sr' unit='mA' dop='0'/>
            <CHANNEL id='99' name='PK_I Rein' unit='mA' dop='0'/>
            <CHANNEL id='100' name='BLDC_ES ist' unit='rpm' dop='0'/>
            <CHANNEL id='101' name='BLDC_ES soll' unit='rpm' dop='0'/>
            <CHANNEL id='102' name='PK_LZ ES seit Füll.' unit='Min' dop='0'/>
            <CHANNEL id='103' name='PK_LZ ES seit Ent.' unit='Min' dop='0'/>
            <CHANNEL id='104' name='PK_Lagerstand' unit='kg' dop='0'/>
            <CHANNEL id='105' name='PK_Verbrauchszähler' unit='kg' dop='0'/>
            <CHANNEL id='106' name='PK_Heiz P Lambda' unit='W' dop='2'/>
            <CHANNEL id='107' name='PK_Heiz U Lambda' unit='V'/>
            <CHANNEL id='108' name='PK_Heiz I Lambda' unit='mA' dop='0'/>
            <CHANNEL id='109' name='PK_Sens U Lambda' unit='mV' dop='0'/>
            <CHANNEL id='110' name='T Spülung' unit='°C'/>
            <CHANNEL id='111' name='PK_UsePos' dop='0'/>
            <CHANNEL id='112' name='PK_AUPSoll' unit='mm'/>
            <CHANNEL id='113' name='PK_AUPIst' unit='mm'/>
            <CHANNEL id='114' name='PK_AUPStrom' unit='mA'/>
            <CHANNEL id='115' name='HKR Anf' unit='°C'/>
            <CHANNEL id='116' name='Anf. HKR0' unit='°C' dop='0'/>
            <CHANNEL id='117' name='Anf. HKR1' unit='°C' dop='0'/>
            <CHANNEL id='118' name='Anf. HKR2' unit='°C' dop='0'/>
            <CHANNEL id='119' name='Anf. HKR3' unit='°C' dop='0'/>
            <CHANNEL id='120' name='Anf. HKR4' unit='°C' dop='0'/>
            <CHANNEL id='121' name='Anf. HKR5' unit='°C' dop='0'/>
            <CHANNEL id='122' name='Anf. HKR6' unit='°C' dop='0'/>
            <CHANNEL id='123' name='Anf. HKR7' unit='°C' dop='0'/>
            <CHANNEL id='124' name='Anf. HKR8' unit='°C' dop='0'/>
            <CHANNEL id='125' name='Anf. HKR9' unit='°C' dop='0'/>
            <CHANNEL id='126' name='Anf. HKR10' unit='°C' dop='0'/>
            <CHANNEL id='127' name='Anf. HKR11' unit='°C' dop='0'/>
            <CHANNEL id='128' name='Anf. HKR12' unit='°C' dop='0'/>
            <CHANNEL id='129' name='Anf. HKR13' unit='°C' dop='0'/>
            <CHANNEL id='130' name='Anf. HKR14' unit='°C' dop='0'/>
            <CHANNEL id='131' name='Anf. HKR15' unit='°C' dop='0'/>
            <CHANNEL id='132' name='Wasserdruck' unit='bar' dop='2'/>
        </ANALOG>
        <DIGITAL>
            <CHANNEL id='0' bit='0' name='Störung'/>
            <CHANNEL id='0' bit='1' name='STB'/>
            <CHANNEL id='0' bit='2' name='TKS'/>
            <CHANNEL id='0' bit='4' name='RLm_auf'/>
            <CHANNEL id='0' bit='5' name='RLm_zu'/>
            <CHANNEL id='0' bit='10' name='WS freig.'/>
            <CHANNEL id='0' bit='11' name='Akt. Code'/>
            <CHANNEL id='0' bit='14' name='FW Freig.'/>
            <CHANNEL id='0' bit='15' name='gFlP'/>
            <CHANNEL id='0' bit='16' name='gFlM auf'/>
            <CHANNEL id='0' bit='17' name='gFlM zu'/>
            <CHANNEL id='0' bit='18' name='gFl2P'/>
            <CHANNEL id='0' bit='19' name='gFl2M auf'/>
            <CHANNEL id='0' bit='20' name='gFl2M zu'/>
            <CHANNEL id='1' bit='0' name='Lamdaheiz.'/>
            <CHANNEL id='1' bit='1' name='Zündheiz.'/>
            <CHANNEL id='1' bit='2' name='FW Pumpe'/>
            <CHANNEL id='1' bit='3' name='FLP'/>
            <CHANNEL id='1' bit='4' name='SLK_auf'/>
            <CHANNEL id='1' bit='5' name='SLK_zu'/>
            <CHANNEL id='1' bit='6' name='PLK_auf'/>
            <CHANNEL id='1' bit='7' name='PLK_zu'/>
            <CHANNEL id='1' bit='8' name='Geb. Relais'/>
            <CHANNEL id='1' bit='9' name='Schnellladev.'/>
            <CHANNEL id='2' bit='0' name='HKPA'/>
            <CHANNEL id='2' bit='1' name='MAA'/>
            <CHANNEL id='2' bit='2' name='MAZ'/>
            <CHANNEL id='2' bit='3' name='HKP1'/>
            <CHANNEL id='2' bit='4' name='M1A'/>
            <CHANNEL id='2' bit='5' name='M1Z'/>
            <CHANNEL id='2' bit='6' name='HKP2'/>
            <CHANNEL id='2' bit='7' name='M2A'/>
            <CHANNEL id='2' bit='8' name='M2Z'/>
            <CHANNEL id='2' bit='9' name='HKP3'/>
            <CHANNEL id='2' bit='10' name='M3A'/>
            <CHANNEL id='2' bit='11' name='M3Z'/>
            <CHANNEL id='2' bit='12' name='HKP4'/>
            <CHANNEL id='2' bit='13' name='M4A'/>
            <CHANNEL id='2' bit='14' name='M4Z'/>
            <CHANNEL id='2' bit='15' name='HKP5'/>
            <CHANNEL id='2' bit='16' name='M5A'/>
            <CHANNEL id='2' bit='17' name='M5Z'/>
            <CHANNEL id='2' bit='18' name='HKP6'/>
            <CHANNEL id='2' bit='19' name='M6A'/>
            <CHANNEL id='2' bit='20' name='M6Z'/>
            <CHANNEL id='2' bit='21' name='HKPB'/>
            <CHANNEL id='2' bit='22' name='MBA'/>
            <CHANNEL id='2' bit='23' name='MBZ'/>
            <CHANNEL id='3' bit='0' name='BPA'/>
            <CHANNEL id='3' bit='1' name='BP1'/>
            <CHANNEL id='3' bit='2' name='BP2'/>
            <CHANNEL id='3' bit='3' name='BP3'/>
            <CHANNEL id='3' bit='4' name='BPB'/>
            <CHANNEL id='3' bit='5' name='ZP Boi.A'/>
            <CHANNEL id='3' bit='6' name='ZP Boi.1'/>
            <CHANNEL id='3' bit='7' name='ZP Boi.2'/>
            <CHANNEL id='3' bit='8' name='ZP Boi.3'/>
            <CHANNEL id='3' bit='9' name='ZP Boi.B'/>
            <CHANNEL id='5' bit='0' name='PK_L Heiz.'/>
            <CHANNEL id='5' bit='1' name='PK_Z Heiz.'/>
            <CHANNEL id='5' bit='2' name='PK_Z Geb.'/>
            <CHANNEL id='5' bit='3' name='PK_LambdaOk'/>
            <CHANNEL id='5' bit='4' name='PK_Fuellstand'/>
            <CHANNEL id='5' bit='5' name='PK_Aschebox'/>
            <CHANNEL id='5' bit='6' name='PK_ES Run'/>
            <CHANNEL id='5' bit='7' name='PK_ES Dir'/>
            <CHANNEL id='5' bit='8' name='PK_AS Saug'/>
            <CHANNEL id='5' bit='9' name='PK_AS RA Run'/>
            <CHANNEL id='5' bit='10' name='PK_AS RA Dir'/>
            <CHANNEL id='5' bit='11' name='PK_Rein En'/>
            <CHANNEL id='5' bit='12' name='PK_Rein Run'/>
            <CHANNEL id='5' bit='13' name='PK_AA Run'/>
            <CHANNEL id='5' bit='14' name='PK_AA Dir'/>
            <CHANNEL id='5' bit='15' name='PK_RLm_auf'/>
            <CHANNEL id='5' bit='16' name='PK_RLm_zu'/>
            <CHANNEL id='5' bit='17' name='PK_RL Pumpe'/>
            <CHANNEL id='5' bit='18' name='PK_RL Verz Aktiv'/>
            <CHANNEL id='5' bit='19' name='Spülung Aktiv'/>
            <CHANNEL id='6' bit='0' name='ExtHK Anf'/>
            <CHANNEL id='6' bit='1' name='ExtHK_2 Anf'/>
            <CHANNEL id='6' bit='2' name='ExtHK_3 Anf'/>
            <CHANNEL id='6' bit='3' name='ExtHK Pumpe'/>
            <CHANNEL id='6' bit='4' name='ExtHK_2 Pumpe'/>
            <CHANNEL id='6' bit='5' name='ExtHK_3 Pumpe'/>
            <CHANNEL id='6' bit='6' name='ExtHK vorh'/>
            <CHANNEL id='6' bit='7' name='ExtHK_2 vorh'/>
            <CHANNEL id='6' bit='8' name='ExtHK_3 vorh'/>
            <CHANNEL id='7' bit='0' name='DReg P2'/>
            <CHANNEL id='7' bit='1' name='DReg P3'/>
            <CHANNEL id='7' bit='2' name='DReg Mi auf'/>
            <CHANNEL id='7' bit='3' name='DReg Mi zu'/>
            <CHANNEL id='7' bit='5' name='DReg2 P2'/>
            <CHANNEL id='7' bit='6' name='DReg2 Mi auf'/>
            <CHANNEL id='7' bit='7' name='DReg2 Mi zu'/>
            <CHANNEL id='7' bit='9' name='DReg3 P2'/>
            <CHANNEL id='7' bit='10' name='DReg3 P3'/>
            <CHANNEL id='7' bit='11' name='DReg3 Mi auf'/>
            <CHANNEL id='7' bit='12' name='DReg3 Mi zu'/>
        </DIGITAL>
    </DAQPRJ>"""


class FieldFormatter:
    def __init__(self, name):
        self._name = name

    def convertValue(self, value):
        return value

    def getName(self):
        return self._name


class NumberFormatter(FieldFormatter):
    def __init__(self, name):
        super().__init__(name)

    def convertValue(self, value):
        try:
            return "{:.2f}".format(float(value))
        except:
            # print("cant convert value", self.getName(), value)
            return value


class BinaryFormatter(FieldFormatter):
    def __init__(self, name):
        super().__init__(name)

    def convertValue(self, value):
        if value.lower() in ["true", "1"]:
            return "true"
        else:
            return "false"


class MappingFormatter(FieldFormatter):
    def __init__(self, name, mapping):
        super().__init__(name)
        self._mapping = mapping

    def convertValue(self, value):
        try:
            return self._mapping[value]
        except:
            try:
                return self._mapping[int(value)]
            except:
                # print("cant convert value to mapping", self.getName(), value, self._mapping)
                return value


_HV_STATES = [
    "Init",
    "Aus",
    "Zündung warten",
    "Zündung",
    "Anheizen",
    "Grundglut",
    "Leistungsbrand",
    "zu Teillast",
    "Teillast",
    "Ausbrand",
    "Gluterhaltung",
    "Restwärme",
    "Übertemperatur",
    "Tür offen",
    "Tür geschlossen",
    "Rauchfangkehrer",
    "TÜV",
    "ABS",
    "STB",
    "Hand"
]

_PK_STATES = [
    "Init",
    "Aus",
    "Schieberost Init",
    "Start",
    "Zündung Einschug",
    "Zündung Pause",
    "Zündung Reduziert",
    "Leistungsbrand",
    "Gluterhaltung",
    "Entaschung",
    "Entaschung Rost",
    "Entaschung Nachlauf",
    "Reinigung",
    "Füllen Start",
    "Füllen",
    "Hand"
]

_HV_MODES = [
    "Unbekannt",
    "Aus",
    "Boiler",
    "Auto",
    "Feuerung Aus"
]

_HK_MODES = [
    "Unbekannt",
    "Auto",
    "Absenken",
    "Heizen",
    "Aus",
    "1x Heizen",
    "1x Absenken"
]

_HK_STATES = [
    "Aus",
    "Heizen",
    "Absenken Rampe",
    "Absenken",
    "Tag/Nacht Abschaltung",
    "Sommerabschaltung",
    "Frostschutz",
    "Estrich",
    "Sommerbadheizen",
    "Hand"
]

_BOI_STATES = [
    "Aus",
    "Ladung aktiv",
    "Übertemperatur",
    "Hand"
]

_PUF_STATES = [
    "Aus",
    "Restwärme",
    "Ein",
    "Ladung aktiv",
    "Hand",
    "RFK"
]

_NOTIFY_MAPPING = {
    "309": "Nachlegen"
}

_FIELD_CONFIG = {
    "ZK": MappingFormatter("HV Status", _HV_STATES),
    "O2": NumberFormatter("HV O2"),
    "O2_soll": NumberFormatter("HV O2 soll"),
    "TK": NumberFormatter("HV Kesseltemperatur"),
    "TKsoll": NumberFormatter("HV Kesseltemperatur soll"),
    "TRL": NumberFormatter("HV Rücklauftemperatur"),
    "TRLsoll": NumberFormatter("HV Rücklauftemperatur soll"),
    "TRG": NumberFormatter("HV Rauchgastemperatur"),
    "Leistung": NumberFormatter("HV Leistung"),
    "SZist": NumberFormatter("HV Saugzug"),
    "SZsoll": NumberFormatter("HV Saugzug soll"),
    "TPo": NumberFormatter("Puffertemperatur oben"),
    "TPm": NumberFormatter("Puffertemperatur mitte"),
    "TPu": NumberFormatter("Puffertemperatur unten"),
    "Spreizung": "Spreizung",
    "RLP/PuffPumpe": "RLP/PuffPumpe",
    "PufLad": NumberFormatter("Pufferfüllgrad"),
    "Störungs Nr": MappingFormatter("Meldung", _NOTIFY_MAPPING),
    "Programm": MappingFormatter("HV Modus", _HV_MODES),
    "Prim.soll": "Prim.soll",
    "Prim.ist": "Prim.ist",
    "Sek.soll": "Sek.soll",
    "Sek.ist": "Sek.ist",
    "Heiz P Lambda": "Heiz P Lambda",
    "Heiz U Lambda": "Heiz U Lambda",
    "Heiz I Lambda": "Heiz I Lambda",
    "Sens U Lambda": "Sens U Lambda",
    "Tplat": "Tplat",
    "TVG": "TVG",
    "TVG2": "TVG2",
    "Taus": NumberFormatter("Außentemperatur"),
    "TA Gem.": NumberFormatter("Außentemperatur gemittelt"),
    "Max Anf Kessel": "Max Anf Kessel",
    "Max Anf ZenPuf": "Max Anf ZenPuf",
    "min.Leist.TRG": "min.Leist.TRG",
    "max.Leist.TRG": "max.Leist.TRG",
    "TFW": "TFW",
    "FW-Anforderung": "FW-Anforderung",
    "Puffer_soll oben": "Puffer_soll oben",
    "Puffer_soll unten": "Puffer_soll unten",
    "PufZustand": MappingFormatter( "Puffer Zustand", _PUF_STATES ),
    "ExtHK Solltmp.": "ExtHK Solltmp.",
    "TVL_A": "TVL_A",
    "TVLs_A": "TVLs_A",
    "TRA_A": "TRA_A",
    "TRs_A": "TRs_A",
    "HKZustand_A": "HKZustand_A",
    "FRA Zustand": "FRA Zustand",
    "TVL_1": NumberFormatter("HK1 Vorlauftemperatur"),
    "TVLs_1": NumberFormatter("HK1 Vorlauftemperatur soll"),
    "TRA_1": NumberFormatter("HK1 Innentemperatur"),
    "TRs_1": "TRs_1",
    "HKZustand_1": MappingFormatter("HK1 Zustand", _HK_STATES),
    "FR1 Zustand": MappingFormatter("HK1 Modus", _HK_MODES),
    "TVL_2": "TVL_2",
    "TVLs_2": "TVLs_2",
    "TRA_2": "TRA_2",
    "TRs_2": "TRs_2",
    "HKZustand_2": "HKZustand_2",
    "FR2 Zustand": "FR2 Zustand",
    "TVL_B": "TVL_B",
    "TVLs_B": "TVLs_B",
    "TRA_B": "TRA_B",
    "TRs_B": "TRs_B",
    "HKZustand_B": "HKZustand_B",
    "FRB Zustand": "FRB Zustand",
    "TBA": "TBA",
    "TBs_A": "TBs_A",
    "TB1": "TB1",
    "TBs_1": "TBs_1",
    "BoiZustand_1": MappingFormatter("Boiler Zustand", _BOI_STATES),
    "TBB": "TBB",
    "TBs_B": "TBs_B",
    "PK_ZK": MappingFormatter("PK Status", _PK_STATES),
    "PK_O2": NumberFormatter("PK O2"),
    "PK_O2soll": NumberFormatter("PK O2 soll"),
    "PK_TK": NumberFormatter("PK Kesseltemperatur"),
    "PK_TKsoll": NumberFormatter("PK Kesseltemperatur soll"),
    "PK_TRL": NumberFormatter("PK Rücklauftemperatur"),
    "PK_TRLsoll": NumberFormatter("PK Rücklauftemperatur soll"),
    "PK_Spreizung": "PK_Spreizung",
    "PK_TRG": NumberFormatter("PK Rauchgastemperatur"),
    "PK_SZ": NumberFormatter("PK Saugzug"),
    "PK_SZs": NumberFormatter("PK Saugzug soll"),
    "PK_Leistung": NumberFormatter("PK Leistung"),
    "PK_ESsoll": "PK_ESsoll",
    "PK_min.Leist.TRG": "PK_min.Leist.TRG",
    "PK_max.Leist.TRG": "PK_max.Leist.TRG",
    "max.Leist.Fuell": "max.Leist.Fuell",
    "max.Leist.TPO": "max.Leist.TPO",
    "PK_ESRegler": "PK_ESRegler",
    "PK_KeBrstScale": "PK_KeBrstScale",
    "PK_Programm": "PK_Programm",
    "PK_RLP": "PK_RLP",
    "PK_Tplat": "PK_Tplat",
    "PK_I Es": "PK_I Es",
    "PK_I Ra": "PK_I Ra",
    "PK_I Aa": "PK_I Aa",
    "PK_I Sr": "PK_I Sr",
    "PK_I Rein": "PK_I Rein",
    "BLDC_ES ist": "BLDC_ES ist",
    "BLDC_ES soll": "BLDC_ES soll",
    "PK_LZ ES seit Füll.": "PK_LZ ES seit Füll.",
    "PK_LZ ES seit Ent.": "PK_LZ ES seit Ent.",
    "PK_Lagerstand": NumberFormatter("Pellets Lagerstand"),
    "PK_Verbrauchszähler": NumberFormatter("Pellets Gesamtverbrauch"),
    "PK_Heiz P Lambda": "PK_Heiz P Lambda",
    "PK_Heiz U Lambda": "PK_Heiz U Lambda",
    "PK_Heiz I Lambda": "PK_Heiz I Lambda",
    "PK_Sens U Lambda": "PK_Sens U Lambda",
    "T Spülung": "T Spülung",
    "PK_UsePos": "PK_UsePos",
    "PK_AUPSoll": "PK_AUPSoll",
    "PK_AUPIst": "PK_AUPIst",
    "PK_AUPStrom": "PK_AUPStrom",
    "HKR Anf": "HKR Anf",
    "Anf. HKR0": "Anf. HKR0",
    "Anf. HKR1": "Anf. HKR1",
    "Anf. HKR2": "Anf. HKR2",
    "Anf. HKR3": "Anf. HKR3",
    "Anf. HKR4": "Anf. HKR4",
    "Anf. HKR5": "Anf. HKR5",
    "Anf. HKR6": "Anf. HKR6",
    "Anf. HKR7": "Anf. HKR7",
    "Anf. HKR8": "Anf. HKR8",
    "Anf. HKR9": "Anf. HKR9",
    "Anf. HKR10": "Anf. HKR10",
    "Anf. HKR11": "Anf. HKR11",
    "Anf. HKR12": "Anf. HKR12",
    "Anf. HKR13": "Anf. HKR13",
    "Anf. HKR14": "Anf. HKR14",
    "Anf. HKR15": "Anf. HKR15",
    "Wasserdruck": NumberFormatter("Wasserdruck"),
    "Störung": BinaryFormatter("Störung"),
    "STB": BinaryFormatter("STB"),
    "TKS": BinaryFormatter("TKS"),
    "RLm_auf": BinaryFormatter("Rücklaufmischer auf"),
    "RLm_zu": BinaryFormatter("Rücklaufmischer zu"),
    "WS freig.": BinaryFormatter("WS freig."),
    "Akt. Code": BinaryFormatter("Akt. Code"),
    "FW Freig.": BinaryFormatter("FW Freig."),
    "gFlP": BinaryFormatter("gFlP"),
    "gFlM auf": BinaryFormatter("gFlM auf"),
    "gFlM zu": BinaryFormatter("gFlM zu"),
    "gFl2P": BinaryFormatter("gFl2P"),
    "gFl2M auf": BinaryFormatter("gFl2M auf"),
    "gFl2M zu": BinaryFormatter("gFl2M zu"),
    "Lamdaheiz.": BinaryFormatter("Lamdaheiz."),
    "Zündheiz.": BinaryFormatter("Zündheiz."),
    "FW Pumpe": BinaryFormatter("FW Pumpe"),
    "FLP": BinaryFormatter("FLP"),
    "SLK_auf": BinaryFormatter("SLK_auf"),
    "SLK_zu": BinaryFormatter("SLK_zu"),
    "PLK_auf": BinaryFormatter("PLK_auf"),
    "PLK_zu": BinaryFormatter("PLK_zu"),
    "Geb. Relais": BinaryFormatter("Geb. Relais"),
    "Schnellladev.": BinaryFormatter("Schnellladev."),
    "HKPA": BinaryFormatter("HKPA"),
    "MAA": BinaryFormatter("MAA"),
    "MAZ": BinaryFormatter("MAZ"),
    "HKP1": BinaryFormatter("HK1 Pumpe"),
    "M1A": BinaryFormatter("M1A"),
    "M1Z": BinaryFormatter("M1Z"),
    "HKP2": BinaryFormatter("HKP2"),
    "M2A": BinaryFormatter("M2A"),
    "M2Z": BinaryFormatter("M2Z"),
    "HKP3": BinaryFormatter("HKP3"),
    "M3A": BinaryFormatter("M3A"),
    "M3Z": BinaryFormatter("M3Z"),
    "HKP4": BinaryFormatter("HKP4"),
    "M4A": BinaryFormatter("M4A"),
    "M4Z": BinaryFormatter("M4Z"),
    "HKP5": BinaryFormatter("HKP5"),
    "M5A": BinaryFormatter("M5A"),
    "M5Z": BinaryFormatter("M5Z"),
    "HKP6": BinaryFormatter("HKP6"),
    "M6A": BinaryFormatter("M6A"),
    "M6Z": BinaryFormatter("M6Z"),
    "HKPB": BinaryFormatter("HKPB"),
    "MBA": BinaryFormatter("MBA"),
    "MBZ": BinaryFormatter("MBZ"),
    "BPA": BinaryFormatter("BPA"),
    "BP1": BinaryFormatter("Boiler 1 Pumpe"),
    "BP2": BinaryFormatter("BP2"),
    "BP3": BinaryFormatter("BP3"),
    "BPB": BinaryFormatter("BPB"),
    "ZP Boi.A": BinaryFormatter("ZP Boi.A"),
    "ZP Boi.1": BinaryFormatter("ZP Boi.1"),
    "ZP Boi.2": BinaryFormatter("ZP Boi.2"),
    "ZP Boi.3": BinaryFormatter("ZP Boi.3"),
    "ZP Boi.B": BinaryFormatter("ZP Boi.B"),
    "PK_L Heiz.": BinaryFormatter("PK_L Heiz."),
    "PK_Z Heiz.": BinaryFormatter("PK_Z Heiz."),
    "PK_Z Geb.": BinaryFormatter("PK_Z Geb."),
    "PK_LambdaOk": BinaryFormatter("PK_LambdaOk"),
    "PK_Fuellstand": BinaryFormatter("PK_Fuellstand"),
    "PK_Aschebox": BinaryFormatter("PK_Aschebox"),
    "PK_ES Run": BinaryFormatter("PK_ES Run"),
    "PK_ES Dir": BinaryFormatter("PK_ES Dir"),
    "PK_AS Saug": BinaryFormatter("PK_AS Saug"),
    "PK_AS RA Run": BinaryFormatter("PK_AS RA Run"),
    "PK_AS RA Dir": BinaryFormatter("PK_AS RA Dir"),
    "PK_Rein En": BinaryFormatter("PK_Rein En"),
    "PK_Rein Run": BinaryFormatter("PK_Rein Run"),
    "PK_AA Run": BinaryFormatter("PK_AA Run"),
    "PK_AA Dir": BinaryFormatter("PK_AA Dir"),
    "PK_RLm_auf": BinaryFormatter("PK Rücklaufmischer auf"),
    "PK_RLm_zu": BinaryFormatter("PK Rücklaufmische rzu"),
    "PK_RL Pumpe": BinaryFormatter("PK Pumpe"),
    "PK_RL Verz Aktiv": BinaryFormatter("PK_RL Verz Aktiv"),
    "Spülung Aktiv": BinaryFormatter("Spülung Aktiv"),
    "ExtHK Anf": BinaryFormatter("ExtHK Anf"),
    "ExtHK_2 Anf": BinaryFormatter("ExtHK_2 Anf"),
    "ExtHK_3 Anf": BinaryFormatter("ExtHK_3 Anf"),
    "ExtHK Pumpe": BinaryFormatter("ExtHK Pumpe"),
    "ExtHK_2 Pumpe": BinaryFormatter("ExtHK_2 Pumpe"),
    "ExtHK_3 Pumpe": BinaryFormatter("ExtHK_3 Pumpe"),
    "ExtHK vorh": BinaryFormatter("ExtHK vorh"),
    "ExtHK_2 vorh": BinaryFormatter("ExtHK_2 vorh"),
    "ExtHK_3 vorh": BinaryFormatter("ExtHK_3 vorh"),
    "DReg P2": BinaryFormatter("DReg P2"),
    "DReg P3": BinaryFormatter("DReg P3"),
    "DReg Mi auf": BinaryFormatter("DReg Mi auf"),
    "DReg Mi zu": BinaryFormatter("DReg Mi zu"),
    "DReg2 P2": BinaryFormatter("DReg2 P2"),
    "DReg2 Mi auf": BinaryFormatter("DReg2 Mi auf"),
    "DReg2 Mi zu": BinaryFormatter("DReg2 Mi zu"),
    "DReg3 P2": BinaryFormatter("DReg3 P2"),
    "DReg3 P3": BinaryFormatter("DReg3 P3"),
    "DReg3 Mi auf": BinaryFormatter("DReg3 Mi auf"),
    "DReg3 Mi zu": BinaryFormatter("DReg3 Mi zu"),
}
