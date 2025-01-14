import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class DataframeInitializer:
    def __init__(self, df2018, df2019, df2020, df2021, df2022, prodi):
        self.df2018 = df2018
        self.df2019 = df2019
        self.df2020 = df2020
        self.df2021 = df2021
        self.df2022 = df2022
        # self.dfUser2018 = dfUser2018
        # self.dfUser2019 = dfUser2019
        # self.dfUser2020 = dfUser2020
        # self.dfUser2021 = dfUser2021
        # self.dfUser2022 = dfUser2022
        self.prodi = prodi

    def cleanse_tracer_data(self):

        # Competence A -> penguasaan kompetensi, B-> peran perguruan tinggi,C-> peran kompetensi
        # Check Space-Valued Data, and replaced by NULL
        self.df2018_competenceA = (
            self.df2018.iloc[:, 6:29].replace(' ', np.nan))
        self.df2018_competenceA.fillna(
            self.df2018_competenceA.mean(), inplace=True)
        self.df2018_competenceB = (self.df2018.iloc[:, 29:52].replace(
            ' ', np.nan))
        self.df2018_competenceB.fillna(
            self.df2018_competenceB.mean(), inplace=True)
        self.df2018_competenceC = (self.df2018.iloc[:, 52:75].replace(
            ' ', np.nan))
        self.df2018_competenceC.fillna(
            self.df2018_competenceC.mean(), inplace=True)
        self.df2019_competenceA = (self.df2019.iloc[:, 7:30].replace(
            ' ', np.nan))
        self.df2019_competenceA.fillna(
            self.df2019_competenceA.mean(), inplace=True)
        self.df2019_competenceB = (self.df2019.iloc[:, 30:53].replace(
            ' ', np.nan))
        self.df2019_competenceB.fillna(
            self.df2019_competenceB.mean(), inplace=True)
        self.df2019_competenceC = (self.df2019.iloc[:, 53:76].replace(
            ' ', np.nan))
        self.df2019_competenceC.fillna(
            self.df2019_competenceC.mean(), inplace=True)
        self.df2020_competenceA = (self.df2020.iloc[:, 7:30].replace(
            ' ', np.nan))
        self.df2020_competenceA.fillna(
            self.df2020_competenceA.mean(), inplace=True)
        self.df2020_competenceB = (self.df2020.iloc[:, 30:53].replace(
            ' ', np.nan))
        self.df2020_competenceB.fillna(
            self.df2020_competenceB.mean(), inplace=True)
        self.df2020_competenceC = (self.df2020.iloc[:, 53:76].replace(
            ' ', np.nan))
        self.df2020_competenceC.fillna(
            self.df2020_competenceC.mean(), inplace=True)
        self.df2021_competenceA = (self.df2021.iloc[:, 8:31].replace(
            ' ', np.nan))
        self.df2021_competenceA.fillna(
            self.df2021_competenceA.mean(), inplace=True)
        self.df2021_competenceB = (self.df2021.iloc[:, 31:54].replace(
            ' ', np.nan))
        self.df2021_competenceB.fillna(
            self.df2021_competenceB.mean(), inplace=True)
        self.df2021_competenceC = (self.df2021.iloc[:, 54:77].replace(
            ' ', np.nan))
        self.df2021_competenceC.fillna(
            self.df2021_competenceC.mean(), inplace=True)
        self.df2022_competenceA = (self.df2022.iloc[:, 8:31].replace(
            ' ', np.nan))
        self.df2022_competenceA.fillna(
            self.df2022_competenceA.mean(), inplace=True)
        self.df2022_competenceB = (self.df2022.iloc[:, 31:54].replace(
            ' ', np.nan))
        self.df2022_competenceB.fillna(
            self.df2022_competenceB.mean(), inplace=True)
        self.df2022_competenceC = (self.df2022.iloc[:, 54:77].replace(
            ' ', np.nan))
        self.df2022_competenceC.fillna(
            self.df2022_competenceC.mean(), inplace=True)

    def init_respondent_data(self):
        self.df2018_competenceA_Prodi = self.df2018_competenceA[
            self.df2018['4. Program Studi'] == self.prodi]
        self.df2018_competenceB_Prodi = self.df2018_competenceB[
            self.df2018['4. Program Studi'] == self.prodi]
        self.df2018_competenceC_Prodi = self.df2018_competenceC[
            self.df2018['4. Program Studi'] == self.prodi]
        self.df2019_competenceA_Prodi = self.df2019_competenceA[
            self.df2019['4. Program Studi'] == self.prodi]
        self.df2019_competenceB_Prodi = self.df2019_competenceB[
            self.df2019['4. Program Studi'] == self.prodi]
        self.df2019_competenceC_Prodi = self.df2019_competenceC[
            self.df2019['4. Program Studi'] == self.prodi]
        self.df2020_competenceA_Prodi = self.df2020_competenceA[
            self.df2020['4. Program Studi'] == self.prodi]
        self.df2020_competenceB_Prodi = self.df2020_competenceB[
            self.df2020['4. Program Studi'] == self.prodi]
        self.df2020_competenceC_Prodi = self.df2020_competenceC[
            self.df2020['4. Program Studi'] == self.prodi]
        self.df2021_competenceA_Prodi = self.df2021_competenceA[
            self.df2021['Program Studi'] == self.prodi]
        self.df2021_competenceB_Prodi = self.df2021_competenceB[
            self.df2021['Program Studi'] == self.prodi]
        self.df2021_competenceC_Prodi = self.df2021_competenceC[
            self.df2021['Program Studi'] == self.prodi]
        self.df2022_competenceA_Prodi = self.df2022_competenceA[
            self.df2022['Program Studi'] == self.prodi]
        self.df2022_competenceB_Prodi = self.df2022_competenceB[
            self.df2022['Program Studi'] == self.prodi]
        self.df2022_competenceC_Prodi = self.df2022_competenceC[
            self.df2022['Program Studi'] == self.prodi]

    def init_competence_data(self):
        self.df2018_competenceA_Prodi = self.df2018_competenceA[
            self.df2018['4. Program Studi'] == self.prodi]
        self.df2018_competenceB_Prodi = self.df2018_competenceB[
            self.df2018['4. Program Studi'] == self.prodi]
        self.df2018_competenceC_Prodi = self.df2018_competenceC[
            self.df2018['4. Program Studi'] == self.prodi]
        self.df2019_competenceA_Prodi = self.df2019_competenceA[
            self.df2019['4. Program Studi'] == self.prodi]
        self.df2019_competenceB_Prodi = self.df2019_competenceB[
            self.df2019['4. Program Studi'] == self.prodi]
        self.df2019_competenceC_Prodi = self.df2019_competenceC[
            self.df2019['4. Program Studi'] == self.prodi]
        self.df2020_competenceA_Prodi = self.df2020_competenceA[
            self.df2020['4. Program Studi'] == self.prodi]
        self.df2020_competenceB_Prodi = self.df2020_competenceB[
            self.df2020['4. Program Studi'] == self.prodi]
        self.df2020_competenceC_Prodi = self.df2020_competenceC[
            self.df2020['4. Program Studi'] == self.prodi]
        self.df2021_competenceA_Prodi = self.df2021_competenceA[
            self.df2021['Program Studi'] == self.prodi]
        self.df2021_competenceB_Prodi = self.df2021_competenceB[
            self.df2021['Program Studi'] == self.prodi]
        self.df2021_competenceC_Prodi = self.df2021_competenceC[
            self.df2021['Program Studi'] == self.prodi]
        self.df2022_competenceA_Prodi = self.df2022_competenceA[
            self.df2022['Program Studi'] == self.prodi]
        self.df2022_competenceB_Prodi = self.df2022_competenceB[
            self.df2022['Program Studi'] == self.prodi]
        self.df2022_competenceC_Prodi = self.df2022_competenceC[
            self.df2022['Program Studi'] == self.prodi]
        self.competencies2018 = ['memecahkan\nmasalah\nkompleks', 'berpikir\nkritis', 'inovasi\ndan/atau\nkreativitas', 'manajemen diri\ndan orang lain',
                                 'bekerja\ntim', 'bekerja\nindividu', 'kecerdasan\nemosional', 'penilaian dan\npengambilan\nkeputusan',
                                 'negosiasi', 'kecerdasan\ndalam\nbertindak', 'kemampuan\nbelajar', 'adaptasi\ndengan\nlingkungan',
                                 'kejujuran\n,loyalitas\n,integritas', 'bekerja dalam\ntekanan', 'etika',
                                 'pengetahuan\n dan penerapan\nbidang/disiplin\nilmu', 'pengetahuan\ndi luar \nbidang/displin\nilmu',
                                 'kemampuan\nanalisis', 'kemampuan \nadministrasi,\nmenuliskan\nlaporan\ndokumen', 'keterampilan\nteknologi\ninformasi dan\nkomunikasi',
                                 'merancang dan atau\nmendesain suatu\nkomponen,sistem\natau proses', 'berkomunikasi\ndengan\nbahasa asing', 'orientasi\nlayanan'
                                 ]

        self.competencies2019 = ['memecahkan\nmasalah\nkompleks', 'berpikir\nkritis', 'inovasi\ndan/atau\nkreativitas', 'manajemen diri\ndan orang lain',
                                 'bekerja\ntim', 'bekerja\nindividu', 'kecerdasan\nemosional', 'penilaian dan\npengambilan\nkeputusan',
                                 'negosiasi', 'kecerdasan\ndalam\nbertindak', 'kemampuan\nbelajar\nsepanjang\nhayat', 'adaptasi\ndengan\nlingkungan',
                                 'kejujuran\n,loyalitas\ndan integritas', 'bekerja dalam\ntekanan', 'etika dan\ntanggung jawab\nkeprofesian', 'kemampuan\nberkomunikasi',
                                 'pengetahuan\n dan penerapan\nbidang/disiplin\nilmu', 'pengetahuan\ndi luar \nbidang/displin\nilmu',
                                 'kemampuan\nanalisis dan\ninterpretasi data', 'kemampuan \nadministrasi,\nmenuliskan\nlaporan\ndokumen', 'keterampilan\nmenggunakan\nteknologi\ninformasi',
                                 'merancang\ndan atau\nmendesain suatu\nkomponen,sistem\natau\nproses', 'kemampuan\nbahasa\nasing'
                                 ]

        self.competencies2020 = self.competencies2019
        self.competencies2021 = self.competencies2019
        self.competencies2022 = self.competencies2019

        # Extract Mean Of Competence Values every year
        self.means2018 = np.array([self.df2018_competenceA_Prodi.mean()[21], self.df2018_competenceA_Prodi.mean()[15], self.df2018_competenceA_Prodi.mean()[14],
                                   self.df2018_competenceA_Prodi.mean()[10], self.df2018_competenceA_Prodi.mean()[
            4], self.df2018_competenceA_Prodi.mean()[19],
            self.df2018_competenceA_Prodi.mean()[19]])

        self.means2019 = np.array([self.df2019_competenceA_Prodi.mean()[22], self.df2019_competenceA_Prodi.mean()[16], self.df2019_competenceA_Prodi.mean()[14],
                                   self.df2019_competenceA_Prodi.mean()[10], self.df2019_competenceA_Prodi.mean()[
            4], self.df2019_competenceA_Prodi.mean()[15],
            self.df2019_competenceA_Prodi.mean()[20]])

        self.means2020 = np.array([self.df2020_competenceA_Prodi.mean()[22], self.df2020_competenceA_Prodi.mean()[16], self.df2020_competenceA_Prodi.mean()[14],
                                   self.df2020_competenceA_Prodi.mean()[10], self.df2020_competenceA_Prodi.mean()[
            4], self.df2020_competenceA_Prodi.mean()[15],
            self.df2020_competenceA_Prodi.mean()[20]])
        self.means2021 = np.array([self.df2021_competenceA_Prodi.mean()[22], self.df2021_competenceA_Prodi.mean()[16], self.df2021_competenceA_Prodi.mean()[14],
                                   self.df2021_competenceA_Prodi.mean()[10], self.df2021_competenceA_Prodi.mean()[
            4], self.df2021_competenceA_Prodi.mean()[15],
            self.df2021_competenceA_Prodi.mean()[20]])
        self.means2022 = np.array([self.df2022_competenceA_Prodi.mean()[22], self.df2022_competenceA_Prodi.mean()[16], self.df2022_competenceA_Prodi.mean()[14],
                                  self.df2022_competenceA_Prodi.mean()[10], self.df2022_competenceA_Prodi.mean()[
            4], self.df2022_competenceA_Prodi.mean()[15],
            self.df2022_competenceA_Prodi.mean()[20]])

        self.categoriesTrend = ["Bahasa\nAsing", "pengetahuan dan\npenerapan bidang/\ndisiplin ilmu", "etika dan tanggung\njawab keprofesian",
                                "kemampuan belajar\nsepanjang hayat", "bekerja tim", "kemampuan\nberkomunikasi", "keterampilan\nmenggunakan\nteknologi informasi"]

    def __filter_zero_workstatus_data(self, arr_workstatus_raw):
        workstatus_filtered = np.array([0, 0, 0, 0, 0])
        if "bekerja" in arr_workstatus_raw:
            workstatus_filtered[0] = arr_workstatus_raw['bekerja']
        if "bekerja dan wiraswasta" in arr_workstatus_raw:
            workstatus_filtered[1] = arr_workstatus_raw['bekerja dan wiraswasta']
        if "wirausaha" in arr_workstatus_raw:
            workstatus_filtered[2] = arr_workstatus_raw['wirausaha']
        if "melanjutkan studi" in arr_workstatus_raw:
            workstatus_filtered[3] = arr_workstatus_raw['melanjutkan studi']
        if "tidak bekerja" in arr_workstatus_raw:
            workstatus_filtered[4] = arr_workstatus_raw['tidak bekerja']

        return workstatus_filtered

    def __filter_zero_workstatus_data_v2(self, arr_workstatus_raw):
        workstatus_filtered = np.array([0, 0, 0, 0, 0])
        if "Bekerja" in arr_workstatus_raw:
            workstatus_filtered[0] = arr_workstatus_raw['Bekerja']
        if "Bekerja dan wiraswasta" in arr_workstatus_raw:
            workstatus_filtered[1] = arr_workstatus_raw['Bekerja dan wiraswasta']
        if "Wirausaha" in arr_workstatus_raw:
            workstatus_filtered[2] = arr_workstatus_raw['Wirausaha']
        if "Melanjutkan studi" in arr_workstatus_raw:
            workstatus_filtered[3] = arr_workstatus_raw['Melanjutkan studi']
        if "Tidak bekerja" in arr_workstatus_raw:
            workstatus_filtered[4] = arr_workstatus_raw['Tidak bekerja']

        return workstatus_filtered

    def init_jobstatus_data(self):
        arr_workstatus_2018 = self.df2018[self.df2018['4. Program Studi']
                                          == self.prodi].iloc[:, 75].value_counts(sort=False)
        arr_workstatus_2019 = self.df2019[self.df2019['4. Program Studi']
                                          == self.prodi].iloc[:, 76].value_counts(sort=False)
        arr_workstatus_2020 = self.df2020[self.df2020['4. Program Studi']
                                          == self.prodi].iloc[:, 76].value_counts(sort=False)
        arr_workstatus_2021 = self.df2021[self.df2021['Program Studi']
                                          == self.prodi].iloc[:, 77].value_counts(sort=False)
        arr_workstatus_2022 = self.df2022[self.df2022['Program Studi']
                                          == self.prodi].iloc[:, 77].value_counts(sort=False)

        # try:
        workstatus_2018 = self.__filter_zero_workstatus_data(
            arr_workstatus_2018)
        workstatus_2019 = self.__filter_zero_workstatus_data(
            arr_workstatus_2019)
        workstatus_2020 = self.__filter_zero_workstatus_data(
            arr_workstatus_2020)
        workstatus_2021 = self.__filter_zero_workstatus_data_v2(
            arr_workstatus_2021)
        workstatus_2022 = self.__filter_zero_workstatus_data_v2(
            arr_workstatus_2022)

        self.workstatus_num = np.array([workstatus_2018,
                                        workstatus_2019,
                                        workstatus_2020,
                                        workstatus_2021,
                                        workstatus_2022])

        self.workstatus_perc = np.array([workstatus_2018/153,
                                         workstatus_2019/141,
                                         workstatus_2020/136,
                                         workstatus_2021/145,
                                         workstatus_2022/94])

    def init_timetogetwork_data(self):
        # Drop the data points that contains no value - 2018
        dfTTGWork2018_raw = self.df2018[["4. Program Studi", "37x. Kapankah Anda memperoleh pekerjaan pertama?",
                                         "37ax. Berapa bulan waktu yang digunakan (sebelum kelulusan) untuk memperoleh pekerjaan pertama?", "37bx. Berapa bulan waktu yang digunakan (sesudah kelulusan) untuk memperoleh pekerjaan pertama?"]]
        # If tidak bekerja, wirausaha,melanjutkan studi/bekerja but contains no value sesudah lulus atua sebelum lulus
        dfTTGWork2018 = dfTTGWork2018_raw.dropna(
            subset=['37x. Kapankah Anda memperoleh pekerjaan pertama?'])

        # Drop the data points that contains no value - 2019
        dfTTGWork2019_raw = self.df2019[["4. Program Studi", "37x. Kapankah Anda memperoleh pekerjaan pertama?",
                                         "37ax. Berapa bulan waktu yang digunakan (sebelum kelulusan) untuk memperoleh pekerjaan pertama?", "37bx. Berapa bulan waktu yang digunakan (sesudah kelulusan) untuk memperoleh pekerjaan pertama?"]]
        # If tidak bekerja, wirausaha,melanjutkan studi/bekerja but contains no value sesudah lulus atua sebelum lulus
        dfTTGWork2019 = dfTTGWork2019_raw.dropna(
            subset=['37x. Kapankah Anda memperoleh pekerjaan pertama?'])

        # Drop the data points that contains no value - 2019
        dfTTGWork2020_raw = self.df2020[["4. Program Studi", "37x. Kapankah Anda memperoleh pekerjaan pertama?",
                                         "37ax. Berapa bulan waktu yang digunakan (sebelum kelulusan) untuk memperoleh pekerjaan pertama?", "37bx. Berapa bulan waktu yang digunakan (sesudah kelulusan) untuk memperoleh pekerjaan pertama?"]]
        # If tidak bekerja, wirausaha,melanjutkan studi/bekerja but contains no value sesudah lulus atua sebelum lulus
        dfTTGWork2020 = dfTTGWork2020_raw.dropna(
            subset=['37x. Kapankah Anda memperoleh pekerjaan pertama?'])

        # Drop the data points that contains no value - 2019
        dfTTGWork2021_raw = self.df2021[["Program Studi", "Kapankah Anda memperoleh pekerjaan pertama?",
                                         "Berapa bulan waktu yang digunakan (sebelum kelulusan) untuk memperoleh pekerjaan pertama?", "Berapa bulan waktu yang digunakan (sesudah kelulusan) untuk memperoleh pekerjaan pertama?"]]
        # If tidak bekerja, wirausaha,melanjutkan studi/bekerja but contains no value sesudah lulus atua sebelum lulus
        dfTTGWork2021 = dfTTGWork2021_raw.dropna(
            subset=['Kapankah Anda memperoleh pekerjaan pertama?'])

        # Drop the data points that contains no value - 2019
        dfTTGWork2022_raw = self.df2022[["Program Studi", "Kapankah Anda memperoleh pekerjaan pertama?",
                                         "Berapa bulan waktu yang digunakan (sebelum kelulusan) untuk memperoleh pekerjaan pertama?", "Berapa bulan waktu yang digunakan (sesudah kelulusan) untuk memperoleh pekerjaan pertama?"]]

        # If tidak bekerja, wirausaha,melanjutkan studi/bekerja but contains no value sesudah lulus atua sebelum lulus
        dfTTGWork2022 = dfTTGWork2022_raw.dropna(
            subset=['Kapankah Anda memperoleh pekerjaan pertama?'])
        # dfTTGWork2018.iloc[230:330]

        # GET PRODI DATAFRAME
        dfTTGWork2018_Prodi = dfTTGWork2018[dfTTGWork2018['4. Program Studi'] == self.prodi]
        self.dfTTGWork2018_Prodi_BeforeGrad = dfTTGWork2018_Prodi[dfTTGWork2018_Prodi[
            "37x. Kapankah Anda memperoleh pekerjaan pertama?"] == "sebelum lulus"]
        self.dfTTGWork2018_Prodi_AfterGrad = dfTTGWork2018_Prodi[dfTTGWork2018_Prodi[
            "37x. Kapankah Anda memperoleh pekerjaan pertama?"] == "sesudah lulus"]

        dfTTGWork2019_Prodi = dfTTGWork2019[dfTTGWork2019['4. Program Studi'] == self.prodi]
        self.dfTTGWork2019_Prodi_BeforeGrad = dfTTGWork2019_Prodi[dfTTGWork2019_Prodi[
            "37x. Kapankah Anda memperoleh pekerjaan pertama?"] == "sebelum lulus"]
        self.dfTTGWork2019_Prodi_AfterGrad = dfTTGWork2019_Prodi[dfTTGWork2019_Prodi[
            "37x. Kapankah Anda memperoleh pekerjaan pertama?"] == "sesudah lulus"]

        dfTTGWork2020_Prodi = dfTTGWork2020[dfTTGWork2020['4. Program Studi'] == self.prodi]
        self.dfTTGWork2020_Prodi_BeforeGrad = dfTTGWork2020_Prodi[dfTTGWork2020_Prodi[
            "37x. Kapankah Anda memperoleh pekerjaan pertama?"] == "sebelum lulus"]
        self.dfTTGWork2020_Prodi_AfterGrad = dfTTGWork2020_Prodi[dfTTGWork2020_Prodi[
            "37x. Kapankah Anda memperoleh pekerjaan pertama?"] == "sesudah lulus"]

        dfTTGWork2021_Prodi = dfTTGWork2021[dfTTGWork2021['Program Studi'] == self.prodi]
        self.dfTTGWork2021_Prodi_BeforeGrad = dfTTGWork2021_Prodi[dfTTGWork2021_Prodi[
            "Kapankah Anda memperoleh pekerjaan pertama?"] == "Sebelum lulus"]
        self.dfTTGWork2021_Prodi_AfterGrad = dfTTGWork2021_Prodi[dfTTGWork2021_Prodi[
            "Kapankah Anda memperoleh pekerjaan pertama?"] == "Sesudah lulus"]

        dfTTGWork2022_Prodi = dfTTGWork2022[dfTTGWork2022['Program Studi'] == self.prodi]
        self.dfTTGWork2022_Prodi_BeforeGrad = dfTTGWork2022_Prodi[dfTTGWork2022_Prodi[
            "Kapankah Anda memperoleh pekerjaan pertama?"] == "Sebelum lulus"]
        self.dfTTGWork2022_Prodi_AfterGrad = dfTTGWork2022_Prodi[dfTTGWork2022_Prodi[
            "Kapankah Anda memperoleh pekerjaan pertama?"] == "Sesudah lulus"]

    def __filter_company_category_data(self, company_category_raw):
        companycat_filtered = np.array([0, 0, 0])
        if "lokal" in company_category_raw:
            companycat_filtered[0] = company_category_raw['lokal']
        if "multinasional" in company_category_raw:
            companycat_filtered[1] = company_category_raw['multinasional']
        if "nasional" in company_category_raw:
            companycat_filtered[2] = company_category_raw['nasional']

        return companycat_filtered

    def __filter_company_category_datav2(self, company_category_raw):
        companycat_filtered = np.array([0, 0, 0])
        if "Lokal" in company_category_raw:
            companycat_filtered[0] = company_category_raw['Lokal']
        if "Multinasional" in company_category_raw:
            companycat_filtered[1] = company_category_raw['Multinasional']
        if "Nasional" in company_category_raw:
            companycat_filtered[2] = company_category_raw['Nasional']

    def init_company_category_data(self):
        dfCompanyCat2018_raw = self.df2018[[
            "4. Program Studi", "A10. Apa kategori perusahaan tempat Anda bekerja?"]]
        dfCompanyCat2018 = dfCompanyCat2018_raw.dropna(
            subset=["A10. Apa kategori perusahaan tempat Anda bekerja?"])

        dfCompanyCat2019_raw = self.df2019[[
            "4. Program Studi", "A10. Apa kategori perusahaan tempat Anda bekerja?"]]
        dfCompanyCat2019 = dfCompanyCat2019_raw.dropna(
            subset=["A10. Apa kategori perusahaan tempat Anda bekerja?"])

        dfCompanyCat2020_raw = self.df2020[[
            "4. Program Studi", "A10. Apa kategori perusahaan tempat Anda bekerja?"]]
        dfCompanyCat2020 = dfCompanyCat2020_raw.dropna(
            subset=["A10. Apa kategori perusahaan tempat Anda bekerja?"])

        dfCompanyCat2021_raw = self.df2021[[
            "Program Studi", "Apa kategori perusahaan tempat Anda bekerja?"]]
        dfCompanyCat2021 = dfCompanyCat2021_raw.dropna(
            subset=["Apa kategori perusahaan tempat Anda bekerja?"])

        dfCompanyCat2022_raw = self.df2022[[
            "Program Studi", "Apa kategori perusahaan tempat Anda bekerja?"]]
        dfCompanyCat2022 = dfCompanyCat2022_raw.dropna(
            subset=["Apa kategori perusahaan tempat Anda bekerja?"])

        dfCompanyCat2018_Prodi = dfCompanyCat2018[dfCompanyCat2018["4. Program Studi"] == self.prodi]
        dfCompanyCat2019_Prodi = dfCompanyCat2019[dfCompanyCat2019["4. Program Studi"] == self.prodi]
        dfCompanyCat2020_Prodi = dfCompanyCat2020[dfCompanyCat2020["4. Program Studi"] == self.prodi]
        dfCompanyCat2021_Prodi = dfCompanyCat2021[dfCompanyCat2021["Program Studi"] == self.prodi]
        dfCompanyCat2022_Prodi = dfCompanyCat2022[dfCompanyCat2022["Program Studi"] == self.prodi]

        valueCompanyCat2018_Prodi = dfCompanyCat2018_Prodi["A10. Apa kategori perusahaan tempat Anda bekerja?"].value_counts(
        ).sort_index()
        valueCompanyCat2019_Prodi = dfCompanyCat2019_Prodi["A10. Apa kategori perusahaan tempat Anda bekerja?"].value_counts(
        ).sort_index()
        valueCompanyCat2020_Prodi = dfCompanyCat2020_Prodi["A10. Apa kategori perusahaan tempat Anda bekerja?"].value_counts(
        ).sort_index()
        valueCompanyCat2021_Prodi = dfCompanyCat2021_Prodi["Apa kategori perusahaan tempat Anda bekerja?"].value_counts(
        ).sort_index()
        valueCompanyCat2022_Prodi = dfCompanyCat2022_Prodi["Apa kategori perusahaan tempat Anda bekerja?"].value_counts(
        ).sort_index()
        self.valueCompanyCat_Prodi = np.array([valueCompanyCat2018_Prodi, valueCompanyCat2019_Prodi,
                                               valueCompanyCat2020_Prodi, valueCompanyCat2021_Prodi,
                                               valueCompanyCat2022_Prodi])
    #def insert_missing_index(y,alphabet):
        #x=pd.DataFrame(y)
        #alphabet =pd.DataFrame(zeros, index = field)
        #already_present_index = x.index.intersection(alphabet.index)
        #missing_index = alphabet.index.difference(x.index)
        #x = pd.concat([y,alphabet.loc[missing_index, :]]).sort_index(ascending=True).fillna(0)

    def init_company_field_data(self):
        #KARENA DATA 2018-2020 MEMISAHKAN ANTARA KATEGORI A (BEKERJA) DAN B (BEKERJA DAN WIRAUSAHA), MAKA HARUS DIGABUNGKAN

        dfCompanyField2018_rawA = self.df2018[[
            "4. Program Studi", "A2. Bidang Usaha"]]
        dfCompanyField2018A = dfCompanyField2018_rawA.dropna(
            subset=["A2. Bidang Usaha"])
        dfCompanyField2018_rawB = self.df2018[[
            "4. Program Studi", "B2. Bidang Usaha"]]
        dfCompanyField2018B = dfCompanyField2018_rawB.dropna(
            subset=["B2. Bidang Usaha"])
        
        dfCompanyField2019_rawA = self.df2019[[
            "4. Program Studi", "A2. Bidang Usaha"]]
        dfCompanyField2019A = dfCompanyField2019_rawA.dropna(
             subset=["A2. Bidang Usaha"])
        dfCompanyField2019_rawB = self.df2019[[
            "4. Program Studi", "B2. Bidang Usaha"]]
        dfCompanyField2019B= dfCompanyField2019_rawB.dropna(
             subset=["B2. Bidang Usaha"])        

        dfCompanyField2020_rawA = self.df2020[[
            "4. Program Studi", "A2. Bidang Usaha"]]
        dfCompanyField2020A = dfCompanyField2020_rawA.dropna(
            subset=["A2. Bidang Usaha"])
        dfCompanyField2020_rawB = self.df2020[[
            "4. Program Studi", "B2. Bidang Usaha"]]
        dfCompanyField2020B = dfCompanyField2020_rawB.dropna(
            subset= ["B2. Bidang Usaha"])
        
        dfCompanyField2021_raw = self.df2021[[
            "Program Studi", "Bidang usaha bekerja"]]
        dfCompanyField2021 = dfCompanyField2021_raw.dropna(
            subset=["Bidang usaha bekerja"])

        dfCompanyField2022_raw = self.df2022[[
            "Program Studi", "Bidang usaha bekerja"]]
        dfCompanyField2022 = dfCompanyField2022_raw.dropna(
            subset=["Bidang usaha bekerja"])

        dfCompanyField2018A_Prodi = dfCompanyField2018A[dfCompanyField2018A["4. Program Studi"] == self.prodi]
        dfCompanyField2018B_Prodi = dfCompanyField2018B[dfCompanyField2018B["4. Program Studi"] == self.prodi]
        dfCompanyField2019A_Prodi = dfCompanyField2019A[dfCompanyField2019A["4. Program Studi"] == self.prodi]
        dfCompanyField2019B_Prodi = dfCompanyField2019B[dfCompanyField2019B["4. Program Studi"] == self.prodi]
        dfCompanyField2020A_Prodi = dfCompanyField2020A[dfCompanyField2020A["4. Program Studi"] == self.prodi]
        dfCompanyField2020B_Prodi = dfCompanyField2020B[dfCompanyField2020B["4. Program Studi"] == self.prodi]
        dfCompanyField2021_Prodi = dfCompanyField2021[dfCompanyField2021["Program Studi"] == self.prodi]
        dfCompanyField2022_Prodi = dfCompanyField2022[dfCompanyField2022["Program Studi"] == self.prodi]

        valueCompanyField2018A_Prodi = dfCompanyField2018A_Prodi["A2. Bidang Usaha"].value_counts(
        ).sort_index()
        valueCompanyField2018B_Prodi = dfCompanyField2018B_Prodi["B2. Bidang Usaha"].value_counts(
        ).sort_index()
        valueCompanyField2019A_Prodi = dfCompanyField2019A_Prodi["A2. Bidang Usaha"].value_counts(
        ).sort_index()
        valueCompanyField2019B_Prodi = dfCompanyField2019B_Prodi["B2. Bidang Usaha"].value_counts(
        ).sort_index()
        valueCompanyField2020A_Prodi = dfCompanyField2020A_Prodi["A2. Bidang Usaha"].value_counts(
        ).sort_index()
        valueCompanyField2020B_Prodi = dfCompanyField2020B_Prodi["B2. Bidang Usaha"].value_counts(
        ).sort_index()

        valueCompanyField2018_Prodi = valueCompanyField2018A_Prodi.add(valueCompanyField2018B_Prodi, fill_value = 0 )
        valueCompanyField2019_Prodi = valueCompanyField2019A_Prodi.add(valueCompanyField2019B_Prodi, fill_value = 0 )
        valueCompanyField2020_Prodi = valueCompanyField2020A_Prodi.add(valueCompanyField2020B_Prodi, fill_value = 0 )

        valueCompanyField2021_Prodi = dfCompanyField2021_Prodi["Bidang usaha bekerja"].value_counts(
        ).sort_index()
        valueCompanyField2022_Prodi = dfCompanyField2022_Prodi["Bidang usaha bekerja"].value_counts(
        ).sort_index()


        

        
       