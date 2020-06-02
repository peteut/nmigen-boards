from nmigen.build import *
from nmigen.vendor.xilinx_7series import *

__all__ = ["CoraZ7Platform"]


class CoraZ7Platform(Xilinx7SeriesPlatform):
    """Platform file for Digilent Cora Z7 board.
    https://reference.digilentinc.com/reference/programmable-logic/cora-z7start"""

    device = "xc7z007s"
    package = "clg400"
    speed = "1"

    def __init__(self):
        super().__init__()

    default_rst = "rst"
    default_clk = "clk"
    resources = [
        Resource("rst", PinsN("D9", dir="i"), Attrs(IOSTANDARD="LVCMOS33")),
        Resource("clk", Pins("H16", dir="i"),
                 Clock(125e6), Attrs(IOSTANDARD="LVCMOS33")),
        Resource("ps", 0,
                 Resource("por", Pins("C7", dir="i")),
                 Resource("rst", Pins("B10", dir="i"),
                          Attrs(IOSTANDARD="LVCMOS18")),  # BTNR
                 Resource("clk", Pins("E7", dir="i"), Clock(50e6)),
                 Attrs(IOSTANDARD="LVCMOS33")),
        *ButtonResources(pins="D20 D19",
                         attrs=Attrs(IOSTANDARD="LVCMOS33")),
        RGBLEDResource(r="N15", g="G17", b="L15",
                       attrs=Attrs(IOSTANDARD="LVCMOS33")),
        RGBLEDResource(r="M15", g="L14", b="G14",
                       attrs=Attrs(IOSTANDARD="LVCMOS33")),
        Resource("i2c", 0,
                 Subsignal("scl", Pins("P16")),
                 Subsignal("sda", Pins("P15")),
                 Attrs(IOSTANDARD="LVCMOS33")),
        Resource("ddr3", 0,
                 Subsignal("rst", Pins("B4", dir="o"),
                           Attrs(IOSTANDARD="SSTL15")),
                 Subsignal("clk",
                           DiffPairs(p="L2", n="M2", dir="o"),
                           Attrs(IOSTANDARD="DIFF_SSTL15")),
                 Subsignal("clk_en", Pins("N3", dir="o"),
                           Attrs(IOSTANDARD="SSTL15")),
                 Subsignal("cs", Pins("N1", dir="o"),
                           Attrs(IOSTANDARD="SSTL15")),
                 Subsignal("we", Pins("M5", dir="o"),
                           Attrs(IOSTANDARD="SSTL15")),
                 Subsignal("ras", Pins("P4", dir="o"),
                           Attrs(IOSTANDARD="SSTL15")),
                 Subsignal("cas", Pins("P5", dir="o"),
                           Attrs(IOSTANDARD="SSTL15")),
                 Subsignal("a",
                           Pins("N2 K2 M3 K3 M4 L1 L4 K4 "
                                "K1 J4 F5 G4 E4 D4 F4", dir="o"),
                           Attrs(IOSTANDARD="SSTL15")),
                 Subsignal("ba",
                           Pins("L5 R4 J5", dir="o"),
                           Attrs(IOSTANDARD="SSTL15")),
                 Subsignal("dqs",
                           DiffPairs(p="C2 G2 R2 W5", n="B2 F2 T2 W4", dir="io"),
                           Attrs(IOSTANDARD="DIFF_SSTL15_DCI")),
                 Subsignal("dq",
                           Pins("C3 B3 A2 A4 D3 D1 C1 E1 "
                                "E2 E3 G3 H3 J3 H2 H1 J1 "
                                "P1 P3 R3 R1 T4 U4 U2 U3 "
                                "V1 Y3 W1 Y4 Y2 W3 V2 V3", dir="io"),
                           Attrs(IOSTANDARD="SSTL15_T_DCI")),
                 Subsignal("dm", Pins("A1 F1 T1 Y1", dir="o"),
                           Attrs(IOSTANDARD="SSTL15")),
                 Subsignal("odt", Pins("N5", dir="o"),
                           Attrs(IOSTANDARD="SSTL15")),
                 )]
    connectors = [
        Connector("j", 1,  # J1
                  "- - L19 M19 N20 P20 P19 R19 T20 T19 U20 V20 W20 K19"),
        Connector("pmod", 0,  # JA
                  "Y18 Y19 Y16 Y17 - - "
                  "U18 U19 W18 W19 - -"),
        Connector("pmod", 1,  # JB
                  "W14 Y14 T11 T10 - - "
                  "V16 W16 V12 W13"),
        Connector("ck_io", 0,
                  "U14 V13 T14 T15 V17 V18 R17 R14 N18 "
                  "M18 U15 K18 J18 G15 - - - - - - - - - - - - "
                  "R16 U12 U13 V15 T15 U17 T17 R18 "),
        Connector("ck_a_io", 0,  # digital input/output
                  "F17 J19 K17 L16 N16 P14"),
        Connector("ck_a", 0,   # anlogue inputs
                  {
                      "a0_p": "E17",  # AD1
                      "a0_n": "D18",
                      "a1_p": "E18",  # AD9
                      "a1_n": "E19",
                      "a2_p": "K14",  # AD6
                      "a2_n": "J14",
                      "a3_p": "K16",  # AD15
                      "a3_n": "J16",
                      "a4_p": "J20",  # AD5
                      "a4_n": "H20",
                      "a5_p": "G19",  # G19
                      "a5_n": "G20",
                      "a6_a7_p": "F19",  # AD12
                      "a6_a7_n": "F20",
                      "a8_a9_p": "C20",  # AD0
                      "a8_a9_n": "B20",
                      "a10_a11_p": "B19",  # AD8
                      "a10_a11_n": "A20",
                  }),
    ]
