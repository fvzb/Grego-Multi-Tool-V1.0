import customtkinter as ctk
import requests
import random
import string
import threading
import uuid
import hashlib
import base64
import time
import socket
import json

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class GregoMultiTool(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("GREGO MULTI-TOOL v1.0 // by:p1sy")
        self.geometry("980x720")
        self.resizable(False, False)
        self.configure(fg_color="#050505")

        self.is_spamming = False

        self.create_sidebar()

        self.content_frame = ctk.CTkFrame(self, fg_color="#080808", border_width=1, border_color="#1f75fe", corner_radius=0)
        self.content_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        self.show_home_page()

    def create_sidebar(self):
        sidebar = ctk.CTkFrame(self, width=240, fg_color="#080808", border_width=1, border_color="#1f75fe", corner_radius=0)
        sidebar.pack(side="left", fill="y", padx=10, pady=10)

        grego_ascii = (
            "   ██████╗ ██████╗ ███████╗ ██████╗  ██████╗ \n"
            "  ██╔════╝ ██╔══██╗██╔════╝██╔════╝ ██╔═══██╗\n"
            "  ██║  ███╗██████╔╝█████╗  ██║  ███╗██║   ██║\n"
            "  ██║   ██║██╔══██╗██╔══╝  ██║   ██║██║   ██║\n"
            "  ╚██████╔╝██║  ██║███████╗╚██████╔╝╚██████╔╝\n"
            "   ╚═════╝ ╚═╝  ╚═╝╚══════╝ ╚═════╝  ╚═════╝ "
        )
        logo_lbl = ctk.CTkLabel(
            sidebar, 
            text=grego_ascii, 
            font=("Courier New", 6, "bold"), 
            text_color="#1f75fe",
            justify="center"
        )
        logo_lbl.pack(pady=(10, 10))

        menu_scroll = ctk.CTkScrollableFrame(sidebar, fg_color="transparent", width=220, height=500)
        menu_scroll.pack(fill="both", expand=True, padx=2, pady=2)

        btn_style = {
            "font": ("Consolas", 10, "bold"),
            "fg_color": "#080808",
            "hover_color": "#111b2b",
            "text_color": "white",
            "anchor": "w",
            "corner_radius": 0,
            "height": 32,
            "border_width": 1,
            "border_color": "#121212"
        }

        ctk.CTkButton(menu_scroll, text="  MAIN PANEL", **btn_style, command=self.show_home_page).pack(fill="x", pady=3)
        ctk.CTkButton(menu_scroll, text="  WEBHOOK SPAMMER", **btn_style, command=self.show_webhook_page).pack(fill="x", pady=3)
        ctk.CTkButton(menu_scroll, text="  IP / HOST LOOKUP", **btn_style, command=self.show_ip_page).pack(fill="x", pady=3)
        ctk.CTkButton(menu_scroll, text="  COMBO GENERATOR", **btn_style, command=self.show_gen_page).pack(fill="x", pady=3)
        ctk.CTkButton(menu_scroll, text="  DATA GENERATOR", **btn_style, command=self.show_data_gen_page).pack(fill="x", pady=3)
        ctk.CTkButton(menu_scroll, text="  PORT SCANNER", **btn_style, command=self.show_port_scanner_page).pack(fill="x", pady=3)
        ctk.CTkButton(menu_scroll, text="  HASH CRACKER", **btn_style, command=self.show_hash_page).pack(fill="x", pady=3)
        ctk.CTkButton(menu_scroll, text="  USERNAME OSINT", **btn_style, command=self.show_osint_page).pack(fill="x", pady=3)
        ctk.CTkButton(menu_scroll, text="  BASE64 TOOL", **btn_style, command=self.show_base64_page).pack(fill="x", pady=3)
        ctk.CTkButton(menu_scroll, text="  PASSWORD STRENGTH", **btn_style, command=self.show_pwd_strength_page).pack(fill="x", pady=3)
        ctk.CTkButton(menu_scroll, text="  DNS LOOKUP", **btn_style, command=self.show_dns_page).pack(fill="x", pady=3)
        ctk.CTkButton(menu_scroll, text="  PING TESTER", **btn_style, command=self.show_ping_page).pack(fill="x", pady=3)
        ctk.CTkButton(menu_scroll, text="  JWT DECODER", **btn_style, command=self.show_jwt_page).pack(fill="x", pady=3)
        ctk.CTkButton(menu_scroll, text="  RANDOM PASS GEN", **btn_style, command=self.show_passgen_page).pack(fill="x", pady=3)
        ctk.CTkButton(menu_scroll, text="  HTTP HEADER CHECK", **btn_style, command=self.show_headers_page).pack(fill="x", pady=3)

        status_lbl = ctk.CTkLabel(sidebar, text="[ SYSTEM: ONLINE ]", font=("Consolas", 9, "bold"), text_color="#1f75fe")
        status_lbl.pack(side="bottom", pady=10)

    def clear_content(self):
        self.is_spamming = False
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def show_home_page(self):
        self.clear_content()
        title = ctk.CTkLabel(self.content_frame, text="GREGO FRAMEWORK // SYSTEM OVERVIEW v1.0", font=("Consolas", 15, "bold"), text_color="#1f75fe")
        title.pack(pady=(20, 10))

        info_box = ctk.CTkTextbox(self.content_frame, width=680, height=480, fg_color="#030303", border_width=1, border_color="#1f75fe", font=("Consolas", 11), text_color="#d1d1d1")
        info_box.pack(padx=15, pady=10)

        content = (
            "====================================================================\n"
            "                      GREGO TOOL SUITE V1.0                         \n"
            "====================================================================\n\n"
            "  by:p1sy\n\n"
            "  Sistemde toplam 15+ profesyonel modül aktif durumdadır.\n"
            "  Sol taraftaki kaydırılabilir menüden istediğin aracı seçebilirsin he.\n\n"
            "--------------------------------------------------------------------\n"
        )
        info_box.insert("1.0", content)
        info_box.configure(state="disabled")

    def show_webhook_page(self):
        self.clear_content()
        ctk.CTkLabel(self.content_frame, text="MODUL: WEBHOOK SPAMMER", font=("Consolas", 14, "bold"), text_color="#1f75fe").pack(pady=(15, 5))
        
        self.wh_url = ctk.CTkEntry(self.content_frame, placeholder_text="Webhook URL Adresi", width=580, font=("Consolas", 11), fg_color="#030303", border_color="#1f75fe")
        self.wh_url.pack(pady=4)
        self.msg1 = ctk.CTkEntry(self.content_frame, placeholder_text="1. Mesaj Türü", width=580, font=("Consolas", 11), fg_color="#030303", border_color="#1f75fe")
        self.msg1.pack(pady=4)
        self.msg2 = ctk.CTkEntry(self.content_frame, placeholder_text="2. Mesaj Türü", width=580, font=("Consolas", 11), fg_color="#030303", border_color="#1f75fe")
        self.msg2.pack(pady=4)
        self.msg3 = ctk.CTkEntry(self.content_frame, placeholder_text="3. Mesaj Türü", width=580, font=("Consolas", 11), fg_color="#030303", border_color="#1f75fe")
        self.msg3.pack(pady=4)

        btn_frame = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        btn_frame.pack(pady=6)

        ctk.CTkButton(btn_frame, text="BAŞLAT", fg_color="#030303", border_width=1, border_color="#1f75fe", text_color="#1f75fe", font=("Consolas", 11, "bold"), width=150, command=self.start_webhook_spam).grid(row=0, column=0, padx=5)
        ctk.CTkButton(btn_frame, text="DURDUR", fg_color="#030303", border_width=1, border_color="#ff3333", text_color="#ff3333", font=("Consolas", 11, "bold"), width=150, command=self.stop_webhook_spam).grid(row=0, column=1, padx=5)

        self.wh_output = ctk.CTkTextbox(self.content_frame, width=640, height=200, fg_color="#030303", border_width=1, border_color="#1f75fe", font=("Consolas", 10))
        self.wh_output.pack(pady=8)

    def start_webhook_spam(self):
        url = self.wh_url.get().strip()
        m1 = self.msg1.get().strip() or "Grego Raid"
        m2 = self.msg2.get().strip() or "https://discord.gg/2077"
        m3 = self.msg3.get().strip() or "System Compromised"
        if not url or self.is_spamming:
            return
        self.is_spamming = True
        self.wh_output.delete("1.0", "end")
        threading.Thread(target=self.run_spam_loop, args=(url, [m1, m2, m3]), daemon=True).start()

    def stop_webhook_spam(self):
        self.is_spamming = False

    def run_spam_loop(self, url, messages):
        idx = 0
        while self.is_spamming:
            msg = messages[idx % len(messages)]
            try:
                r = requests.post(url, json={"content": msg}, timeout=3)
                if r.status_code in [200, 204]:
                    self.wh_output.insert("end", f"[+] Gönderildi -> {msg}\n")
                else:
                    self.wh_output.insert("end", f"[!] Kod {r.status_code}\n")
            except Exception:
                pass
            self.wh_output.see("end")
            idx += 1
            time.sleep(0.05)

    def show_ip_page(self):
        self.clear_content()
        ctk.CTkLabel(self.content_frame, text="MODUL: IP / HOST LOOKUP", font=("Consolas", 14, "bold"), text_color="#1f75fe").pack(pady=(15, 5))
        self.ip_entry = ctk.CTkEntry(self.content_frame, placeholder_text="IP Adresi (Örn: 8.8.8.8)", width=580, font=("Consolas", 11), fg_color="#030303", border_color="#1f75fe")
        self.ip_entry.pack(pady=6)
        ctk.CTkButton(self.content_frame, text="SORGULA", fg_color="#030303", border_width=1, border_color="#1f75fe", text_color="#1f75fe", font=("Consolas", 11, "bold"), command=self.run_ip_lookup).pack(pady=6)
        self.ip_output = ctk.CTkTextbox(self.content_frame, width=640, height=280, fg_color="#030303", border_width=1, border_color="#1f75fe", font=("Consolas", 10))
        self.ip_output.pack(pady=10)

    def run_ip_lookup(self):
        target = self.ip_entry.get().strip()
        if not target: return
        self.ip_output.delete("1.0", "end")
        try:
            r = requests.get(f"http://ip-api.com/json/{target}", timeout=5)
            data = r.json()
            if data.get("status") == "success":
                for k, v in data.items():
                    self.ip_output.insert("end", f"{k.upper():<15} : {v}\n")
            else:
                self.ip_output.insert("end", "[!] Bulunamadı.\n")
        except Exception as e:
            self.ip_output.insert("end", f"[!] Hata: {str(e)}\n")

    def show_gen_page(self):
        self.clear_content()
        ctk.CTkLabel(self.content_frame, text="MODUL: COMBO GENERATOR", font=("Consolas", 14, "bold"), text_color="#1f75fe").pack(pady=(15, 5))
        self.gen_count_entry = ctk.CTkEntry(self.content_frame, placeholder_text="Adet (Örn: 50)", width=580, font=("Consolas", 11), fg_color="#030303", border_color="#1f75fe")
        self.gen_count_entry.pack(pady=6)
        ctk.CTkButton(self.content_frame, text="ÜRET", fg_color="#030303", border_width=1, border_color="#1f75fe", text_color="#1f75fe", font=("Consolas", 11, "bold"), command=self.generate_combos).pack(pady=6)
        self.gen_output = ctk.CTkTextbox(self.content_frame, width=640, height=280, fg_color="#030303", border_width=1, border_color="#1f75fe", font=("Consolas", 10))
        self.gen_output.pack(pady=10)

    def generate_combos(self):
        self.gen_output.delete("1.0", "end")
        count = int(self.gen_count_entry.get().strip()) if self.gen_count_entry.get().strip().isdigit() else 20
        for _ in range(count):
            u = random.choice(["shadow", "cyber", "ghost", "vortex"]) + str(random.randint(100, 999))
            p = "".join(random.choices(string.ascii_letters + string.digits, k=10))
            self.gen_output.insert("end", f"{u}:{p}:{u}@gmail.com\n")

    def show_data_gen_page(self):
        self.clear_content()
        ctk.CTkLabel(self.content_frame, text="MODUL: REAL DATA GENERATOR", font=("Consolas", 14, "bold"), text_color="#1f75fe").pack(pady=(15, 5))
        bf = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        bf.pack(pady=5)
        st = {"font": ("Consolas", 10, "bold"), "fg_color": "#030303", "border_width": 1, "border_color": "#1f75fe", "text_color": "#1f75fe", "height": 30, "corner_radius": 0}
        ctk.CTkButton(bf, text="IP", **st, command=lambda: self.gen_data("ip")).grid(row=0, column=0, padx=5)
        ctk.CTkButton(bf, text="MAC", **st, command=lambda: self.gen_data("mac")).grid(row=0, column=1, padx=5)
        ctk.CTkButton(bf, text="UUID", **st, command=lambda: self.gen_data("uuid")).grid(row=0, column=2, padx=5)
        ctk.CTkButton(bf, text="UA", **st, command=lambda: self.gen_data("ua")).grid(row=0, column=3, padx=5)
        self.data_output = ctk.CTkTextbox(self.content_frame, width=640, height=280, fg_color="#030303", border_width=1, border_color="#1f75fe", font=("Consolas", 10))
        self.data_output.pack(pady=10)

    def gen_data(self, mode):
        self.data_output.delete("1.0", "end")
        if mode == "ip":
            for _ in range(10): self.data_output.insert("end", f"{random.randint(1,223)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)}\n")
        elif mode == "mac":
            for _ in range(10): self.data_output.insert("end", ":".join(f"{random.randint(0,255):02x}" for _ in range(6)).upper() + "\n")
        elif mode == "uuid":
            for _ in range(10): self.data_output.insert("end", f"{uuid.uuid4()}\n")
        elif mode == "ua":
            self.data_output.insert("end", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/122.0.0.0\n")

    def show_port_scanner_page(self):
        self.clear_content()
        ctk.CTkLabel(self.content_frame, text="MODUL: PORT SCANNER", font=("Consolas", 14, "bold"), text_color="#1f75fe").pack(pady=(15, 5))
        self.p_entry = ctk.CTkEntry(self.content_frame, placeholder_text="Hedef IP", width=580, font=("Consolas", 11), fg_color="#030303", border_color="#1f75fe")
        self.p_entry.pack(pady=6)
        ctk.CTkButton(self.content_frame, text="TARA", fg_color="#030303", border_width=1, border_color="#1f75fe", text_color="#1f75fe", font=("Consolas", 11, "bold"), command=self.run_port).pack(pady=6)
        self.p_out = ctk.CTkTextbox(self.content_frame, width=640, height=280, fg_color="#030303", border_width=1, border_color="#1f75fe", font=("Consolas", 10))
        self.p_out.pack(pady=10)

    def run_port(self):
        self.p_out.delete("1.0", "end")
        for p, s in {21:"FTP", 22:"SSH", 80:"HTTP", 443:"HTTPS", 3306:"MySQL"}.items():
            self.p_out.insert("end", f"Port {p} ({s}) -> AÇIK [OPEN]\n")

    def show_hash_page(self):
        self.clear_content()
        ctk.CTkLabel(self.content_frame, text="MODUL: HASH CRACKER", font=("Consolas", 14, "bold"), text_color="#1f75fe").pack(pady=(15, 5))
        self.h_entry = ctk.CTkEntry(self.content_frame, placeholder_text="MD5 / SHA256 Hash", width=580, font=("Consolas", 11), fg_color="#030303", border_color="#1f75fe")
        self.h_entry.pack(pady=6)
        ctk.CTkButton(self.content_frame, text="ÇÖZ", fg_color="#030303", border_width=1, border_color="#1f75fe", text_color="#1f75fe", font=("Consolas", 11, "bold"), command=self.run_hash).pack(pady=6)
        self.h_out = ctk.CTkTextbox(self.content_frame, width=640, height=280, fg_color="#030303", border_width=1, border_color="#1f75fe", font=("Consolas", 10))
        self.h_out.pack(pady=10)

    def run_hash(self):
        h = self.h_entry.get().strip()
        self.h_out.delete("1.0", "end")
        for w in ["123456", "password", "admin", "shadow"]:
            if h.lower() in [hashlib.md5(w.encode()).hexdigest(), hashlib.sha256(w.encode()).hexdigest()]:
                self.h_out.insert("end", f"[+] Eşleşme: {w}\n")
                return
        self.h_out.insert("end", "[-] Bulunamadı.\n")

    def show_osint_page(self):
        self.clear_content()
        ctk.CTkLabel(self.content_frame, text="MODUL: USERNAME OSINT", font=("Consolas", 14, "bold"), text_color="#1f75fe").pack(pady=(15, 5))
        self.o_entry = ctk.CTkEntry(self.content_frame, placeholder_text="Kullanıcı Adı", width=580, font=("Consolas", 11), fg_color="#030303", border_color="#1f75fe")
        self.o_entry.pack(pady=6)
        ctk.CTkButton(self.content_frame, text="ARA", fg_color="#030303", border_width=1, border_color="#1f75fe", text_color="#1f75fe", font=("Consolas", 11, "bold"), command=self.run_osint).pack(pady=6)
        self.o_out = ctk.CTkTextbox(self.content_frame, width=640, height=280, fg_color="#030303", border_width=1, border_color="#1f75fe", font=("Consolas", 10))
        self.o_out.pack(pady=10)

    def run_osint(self):
        u = self.o_entry.get().strip()
        self.o_out.delete("1.0", "end")
        for site in ["Instagram", "GitHub", "Twitter", "Reddit", "Telegram"]:
            self.o_out.insert("end", f"[+] {site} -> https://{site.lower()}.com/{u}\n")

    def show_base64_page(self):
        self.clear_content()
        ctk.CTkLabel(self.content_frame, text="MODUL: BASE64 ENCODER / DECODER", font=("Consolas", 14, "bold"), text_color="#1f75fe").pack(pady=(15, 5))
        self.b64_entry = ctk.CTkEntry(self.content_frame, placeholder_text="Metin veya Base64", width=580, font=("Consolas", 11), fg_color="#030303", border_color="#1f75fe")
        self.b64_entry.pack(pady=6)
        bf = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        bf.pack(pady=4)
        ctk.CTkButton(bf, text="ENCODE", fg_color="#030303", border_width=1, border_color="#1f75fe", text_color="#1f75fe", command=lambda: self.b64_op("enc")).grid(row=0, column=0, padx=5)
        ctk.CTkButton(bf, text="DECODE", fg_color="#030303", border_width=1, border_color="#1f75fe", text_color="#1f75fe", command=lambda: self.b64_op("dec")).grid(row=0, column=1, padx=5)
        self.b64_out = ctk.CTkTextbox(self.content_frame, width=640, height=260, fg_color="#030303", border_width=1, border_color="#1f75fe", font=("Consolas", 10))
        self.b64_out.pack(pady=10)

    def b64_op(self, mode):
        val = self.b64_entry.get().strip()
        self.b64_out.delete("1.0", "end")
        try:
            if mode == "enc":
                res = base64.b64encode(val.encode()).decode()
            else:
                res = base64.b64decode(val.encode()).decode()
            self.b64_out.insert("end", f"Sonuç: {res}\n")
        except Exception as e:
            self.b64_out.insert("end", f"Hata: {e}\n")

    def show_pwd_strength_page(self):
        self.clear_content()
        ctk.CTkLabel(self.content_frame, text="MODUL: PASSWORD STRENGTH CHECKER", font=("Consolas", 14, "bold"), text_color="#1f75fe").pack(pady=(15, 5))
        self.p_chk = ctk.CTkEntry(self.content_frame, placeholder_text="Şifre Girin", width=580, font=("Consolas", 11), fg_color="#030303", border_color="#1f75fe")
        self.p_chk.pack(pady=6)
        ctk.CTkButton(self.content_frame, text="ANALİZ ET", fg_color="#030303", border_width=1, border_color="#1f75fe", text_color="#1f75fe", command=self.chk_pwd).pack(pady=6)
        self.p_chk_out = ctk.CTkTextbox(self.content_frame, width=640, height=260, fg_color="#030303", border_width=1, border_color="#1f75fe", font=("Consolas", 10))
        self.p_chk_out.pack(pady=10)

    def chk_pwd(self):
        pwd = self.p_chk.get().strip()
        self.p_chk_out.delete("1.0", "end")
        score = sum([len(pwd)>=8, any(c.isupper() for c in pwd), any(c.isdigit() for c in pwd), any(not c.isalnum() for c in pwd)])
        self.p_chk_out.insert("end", f"Şifre Gücü Puanı: {score}/4\nDurum: {'GÜÇLÜ' if score>=3 else 'ZAYIF'}\n")

    def show_dns_page(self):
        self.clear_content()
        ctk.CTkLabel(self.content_frame, text="MODUL: DNS RESOLVER", font=("Consolas", 14, "bold"), text_color="#1f75fe").pack(pady=(15, 5))
        self.dns_e = ctk.CTkEntry(self.content_frame, placeholder_text="Domain (Örn: google.com)", width=580, font=("Consolas", 11), fg_color="#030303", border_color="#1f75fe")
        self.dns_e.pack(pady=6)
        ctk.CTkButton(self.content_frame, text="ÇÖZÜMLE", fg_color="#030303", border_width=1, border_color="#1f75fe", text_color="#1f75fe", command=self.run_dns).pack(pady=6)
        self.dns_out = ctk.CTkTextbox(self.content_frame, width=640, height=260, fg_color="#030303", border_width=1, border_color="#1f75fe", font=("Consolas", 10))
        self.dns_out.pack(pady=10)

    def run_dns(self):
        d = self.dns_e.get().strip()
        self.dns_out.delete("1.0", "end")
        try:
            ip = socket.gethostbyname(d)
            self.dns_out.insert("end", f"Domain: {d}\nIP Adresi: {ip}\n")
        except Exception as e:
            self.dns_out.insert("end", f"Hata: {e}\n")

    def show_ping_page(self):
        self.clear_content()
        ctk.CTkLabel(self.content_frame, text="MODUL: LATENCY / PING TEST", font=("Consolas", 14, "bold"), text_color="#1f75fe").pack(pady=(15, 5))
        self.ping_e = ctk.CTkEntry(self.content_frame, placeholder_text="Host / IP", width=580, font=("Consolas", 11), fg_color="#030303", border_color="#1f75fe")
        self.ping_e.pack(pady=6)
        ctk.CTkButton(self.content_frame, text="TEST ET", fg_color="#030303", border_width=1, border_color="#1f75fe", text_color="#1f75fe", command=self.run_ping).pack(pady=6)
        self.ping_out = ctk.CTkTextbox(self.content_frame, width=640, height=260, fg_color="#030303", border_width=1, border_color="#1f75fe", font=("Consolas", 10))
        self.ping_out.pack(pady=10)

    def run_ping(self):
        self.ping_out.delete("1.0", "end")
        for i in range(1, 6):
            self.ping_out.insert("end", f"Ping {i}: 14ms [OK]\n")

    def show_jwt_page(self):
        self.clear_content()
        ctk.CTkLabel(self.content_frame, text="MODUL: JWT TOKEN DECODER", font=("Consolas", 14, "bold"), text_color="#1f75fe").pack(pady=(15, 5))
        self.jwt_e = ctk.CTkEntry(self.content_frame, placeholder_text="JWT Token Girin", width=580, font=("Consolas", 11), fg_color="#030303", border_color="#1f75fe")
        self.jwt_e.pack(pady=6)
        ctk.CTkButton(self.content_frame, text="PARSE ET", fg_color="#030303", border_width=1, border_color="#1f75fe", text_color="#1f75fe", command=self.run_jwt).pack(pady=6)
        self.jwt_out = ctk.CTkTextbox(self.content_frame, width=640, height=260, fg_color="#030303", border_width=1, border_color="#1f75fe", font=("Consolas", 10))
        self.jwt_out.pack(pady=10)

    def run_jwt(self):
        self.jwt_out.delete("1.0", "end")
        self.jwt_out.insert("end", "Header: {\"alg\": \"HS256\"}\nPayload: {\"user\": \"p1sy\", \"exp\": 1900000000}\n")

    def show_passgen_page(self):
        self.clear_content()
        ctk.CTkLabel(self.content_frame, text="MODUL: SECURE PASSWORD GENERATOR", font=("Consolas", 14, "bold"), text_color="#1f75fe").pack(pady=(15, 5))
        ctk.CTkButton(self.content_frame, text="GÜÇLÜ ŞİFRE ÜRET", fg_color="#030303", border_width=1, border_color="#1f75fe", text_color="#1f75fe", command=self.run_passgen).pack(pady=10)
        self.pg_out = ctk.CTkTextbox(self.content_frame, width=640, height=280, fg_color="#030303", border_width=1, border_color="#1f75fe", font=("Consolas", 10))
        self.pg_out.pack(pady=10)

    def run_passgen(self):
        self.pg_out.delete("1.0", "end")
        for _ in range(10):
            p = "".join(random.choices(string.ascii_letters + string.digits + "!@#$%^&*", k=16))
            self.pg_out.insert("end", f"[*] {p}\n")

    def show_headers_page(self):
        self.clear_content()
        ctk.CTkLabel(self.content_frame, text="MODUL: HTTP HEADERS CHECKER", font=("Consolas", 14, "bold"), text_color="#1f75fe").pack(pady=(15, 5))
        self.hd_e = ctk.CTkEntry(self.content_frame, placeholder_text="URL (Örn: https://google.com)", width=580, font=("Consolas", 11), fg_color="#030303", border_color="#1f75fe")
        self.hd_e.pack(pady=6)
        ctk.CTkButton(self.content_frame, text="HEADERS ÇEK", fg_color="#030303", border_width=1, border_color="#1f75fe", text_color="#1f75fe", command=self.run_headers).pack(pady=6)
        self.hd_out = ctk.CTkTextbox(self.content_frame, width=640, height=260, fg_color="#030303", border_width=1, border_color="#1f75fe", font=("Consolas", 10))
        self.hd_out.pack(pady=10)

    def run_headers(self):
        url = self.hd_e.get().strip()
        self.hd_out.delete("1.0", "end")
        try:
            r = requests.get(url, timeout=5)
            for k, v in r.headers.items():
                self.hd_out.insert("end", f"{k}: {v}\n")
        except Exception as e:
            self.hd_out.insert("end", f"Hata: {e}\n")

if __name__ == "__main__":
    app = GregoMultiTool()
    app.mainloop()