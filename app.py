import webbrowser
import tkinter as tk
import customtkinter as ctk

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class SEOCalculator(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("SEO & Marketing Calculator")
        self.geometry("600x720")
        self.resizable(False, False)

        # Заголовок
        self.header = ctk.CTkLabel(
            self, 
            text="Калькулятор SEO и Маркетинга", 
            font=ctk.CTkFont(size=22, weight="bold")
        )
        self.header.pack(pady=(15, 5))

        # Создание вкладок
        self.tabview = ctk.CTkTabview(self, width=560, height=560)
        self.tabview.pack(padx=20, pady=5)

        self.tabview.add("Основные (CTR, CPM, CPC)")
        self.tabview.add("Конверсии (CR, CPA, CPL, CPI, CPO)")
        self.tabview.add("Эффективность (ROI, ДРР)")

        self.setup_traffic_tab()
        self.setup_conversion_tab()
        self.setup_roi_tab()

        # --- Подвал (Footer) ---
        self.footer_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.footer_frame.pack(side="bottom", fill="x", pady=10)

        self.dev_label = ctk.CTkLabel(
            self.footer_frame, 
            text="Разработчик: ", 
            font=ctk.CTkFont(size=12)
        )
        self.dev_label.pack(side="left", padx=(180, 0))

        self.tg_link = ctk.CTkLabel(
            self.footer_frame, 
            text="Timur Qobilov: @timurqobilov", 
            font=ctk.CTkFont(size=12, weight="bold", underline=True),
            text_color="#3B82F6",
            cursor="hand2"
        )
        self.tg_link.pack(side="left")
        self.tg_link.bind("<Button-1>", lambda e: webbrowser.open_new("https://t.me/timurqobilov"))

    def create_input(self, parent, label_text, row):
        lbl = ctk.CTkLabel(parent, text=label_text, anchor="w", font=ctk.CTkFont(size=13))
        lbl.grid(row=row, column=0, padx=15, pady=6, sticky="w")
        
        entry = ctk.CTkEntry(parent, width=180, placeholder_text="0")
        entry.grid(row=row, column=1, padx=15, pady=6)
        return entry

    def create_result(self, parent, label_text, row):
        lbl = ctk.CTkLabel(parent, text=label_text, font=ctk.CTkFont(size=13, weight="bold"), anchor="w")
        lbl.grid(row=row, column=0, padx=15, pady=6, sticky="w")
        
        val_lbl = ctk.CTkLabel(parent, text="—", font=ctk.CTkFont(size=13, weight="bold"), text_color="#1F6AA5", anchor="e")
        val_lbl.grid(row=row, column=1, padx=15, pady=6, sticky="e")
        return val_lbl

    # --- Вкладка 1: Трафик и расходы ---
    def setup_traffic_tab(self):
        tab = self.tabview.tab("Основные (CTR, CPM, CPC)")

        self.cost_t1 = self.create_input(tab, "Расходы / Бюджет (руб):", 0)
        self.impressions_t1 = self.create_input(tab, "Показы (Impressions):", 1)
        self.clicks_t1 = self.create_input(tab, "Клики (Clicks):", 2)

        btn = ctk.CTkButton(tab, text="Рассчитать", command=self.calc_traffic)
        btn.grid(row=3, column=0, columnspan=2, pady=15)

        self.res_ctr = self.create_result(tab, "CTR (Click-Through Rate):", 4)
        self.res_cpm = self.create_result(tab, "CPM (Cost per 1000):", 5)
        self.res_cpc = self.create_result(tab, "CPC (Cost per Click):", 6)

    def calc_traffic(self):
        try:
            cost = float(self.cost_t1.get() or 0)
            impressions = float(self.impressions_t1.get() or 0)
            clicks = float(self.clicks_t1.get() or 0)

            ctr = (clicks / impressions * 100) if impressions > 0 else 0
            cpm = (cost / impressions * 1000) if impressions > 0 else 0
            cpc = (cost / clicks) if clicks > 0 else 0

            self.res_ctr.configure(text=f"{ctr:.2f} %")
            self.res_cpm.configure(text=f"{cpm:.2f} руб.")
            self.res_cpc.configure(text=f"{cpc:.2f} руб.")
        except ValueError:
            pass

    # --- Вкладка 2: Конверсии ---
    def setup_conversion_tab(self):
        tab = self.tabview.tab("Конверсии (CR, CPA, CPL, CPI, CPO)")

        self.cost_t2 = self.create_input(tab, "Расходы (руб):", 0)
        self.clicks_t2 = self.create_input(tab, "Клики / Переходы:", 1)
        self.actions_t2 = self.create_input(tab, "Целевые действия (CPA):", 2)
        self.leads_t2 = self.create_input(tab, "Лиды / Заявки (CPL):", 3)
        self.installs_t2 = self.create_input(tab, "Установки (CPI):", 4)
        self.orders_t2 = self.create_input(tab, "Заказы / Продажи (CPO):", 5)

        btn = ctk.CTkButton(tab, text="Рассчитать", command=self.calc_conversions)
        btn.grid(row=6, column=0, columnspan=2, pady=10)

        self.res_cr = self.create_result(tab, "CR (Conversion Rate):", 7)
        self.res_cpa = self.create_result(tab, "CPA (Cost per Action):", 8)
        self.res_cpl = self.create_result(tab, "CPL (Cost per Lead):", 9)
        self.res_cpi = self.create_result(tab, "CPI (Cost per Install):", 10)
        self.res_cpo = self.create_result(tab, "CPO (Cost per Order):", 11)

    def calc_conversions(self):
        try:
            cost = float(self.cost_t2.get() or 0)
            clicks = float(self.clicks_t2.get() or 0)
            actions = float(self.actions_t2.get() or 0)
            leads = float(self.leads_t2.get() or 0)
            installs = float(self.installs_t2.get() or 0)
            orders = float(self.orders_t2.get() or 0)

            total_conversions = actions + leads + installs + orders
            cr = (total_conversions / clicks * 100) if clicks > 0 else 0

            cpa = (cost / actions) if actions > 0 else 0
            cpl = (cost / leads) if leads > 0 else 0
            cpi = (cost / installs) if installs > 0 else 0
            cpo = (cost / orders) if orders > 0 else 0

            self.res_cr.configure(text=f"{cr:.2f} %")
            self.res_cpa.configure(text=f"{cpa:.2f} руб." if cpa else "—")
            self.res_cpl.configure(text=f"{cpl:.2f} руб." if cpl else "—")
            self.res_cpi.configure(text=f"{cpi:.2f} руб." if cpi else "—")
            self.res_cpo.configure(text=f"{cpo:.2f} руб." if cpo else "—")
        except ValueError:
            pass

    # --- Вкладка 3: Финансовая эффективность ---
    def setup_roi_tab(self):
        tab = self.tabview.tab("Эффективность (ROI, ДРР)")

        self.cost_t3 = self.create_input(tab, "Расходы на рекламу/SEO (руб):", 0)
        self.revenue_t3 = self.create_input(tab, "Доход / Выручка (руб):", 1)

        btn = ctk.CTkButton(tab, text="Рассчитать", command=self.calc_financials)
        btn.grid(row=2, column=0, columnspan=2, pady=15)

        self.res_roi = self.create_result(tab, "ROI / ROMI:", 3)
        self.res_drr = self.create_result(tab, "ДРР (Доля рекламных расходов):", 4)

    def calc_financials(self):
        try:
            cost = float(self.cost_t3.get() or 0)
            revenue = float(self.revenue_t3.get() or 0)

            roi = ((revenue - cost) / cost * 100) if cost > 0 else 0
            drr = (cost / revenue * 100) if revenue > 0 else 0

            roi_color = "#2FA572" if roi >= 0 else "#D55252"

            self.res_roi.configure(text=f"{roi:.2f} %", text_color=roi_color)
            self.res_drr.configure(text=f"{drr:.2f} %")
        except ValueError:
            pass


if __name__ == "__main__":
    app = SEOCalculator()
    app.mainloop()