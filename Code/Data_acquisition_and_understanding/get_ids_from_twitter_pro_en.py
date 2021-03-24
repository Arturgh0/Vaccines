import twint

# Configure
c = twint.Config()
c.Custom["tweet"] = ["id"]
c.Search = "#ProVaccine OR #VaccinesSaveLives OR #ProVaxxer OR #ProVax, ProVaxx OR #VaccinesWork OR #VaccineForAll OR #VaccinesForAll OR #GetVaccinated OR #NOTanantivaxxer OR #IWillGetVaccinated OR #VaccinesAreSafe OR #VaccinesSave OR #VaccineSave OR #VaccinesNow OR #VaccinesAreGood OR #TrustVaccines OR #ITrustVaccines OR #IGotTheShot OR #IGotVaccinated OR #Vaccinated OR #VaccinationNow OR #VaccineWork OR #VaccineSaveLives OR #VaccinesAreGreat"
c.Since = "2019-03-01"
c.until = "2021-03-01"
c.Lang = "pt"
c.Output = "../../Data/Raw/ids_pro_en.csv"
c.Store_csv = True

# Run
twint.run.Search(c)
