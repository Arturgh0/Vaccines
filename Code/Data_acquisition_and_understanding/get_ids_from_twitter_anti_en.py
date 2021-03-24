import twint

# Configure
c = twint.Config()
c.Custom["tweet"] = ["id"]
c.Search = "#VaccinesCauseAutism OR #VaccinesAreBad OR #VaccinesAreDangerous OR #VaccinesKill OR #AntiVaccine OR #NoVaccineForMe OR #DontTrustVaccines OR #IWontTakeIt OR #VaccineConspiracy OR #IWontGetVaccinated OR #VaccinesCauseCancer OR #DontGetVaccinated OR #VaccineKill OR #VaccineDontWork OR #AgainstVaccination OR #VaccineChip OR #VaccineDangerous OR #VaccineDeath OR #AvoidVaccine OR #VaccineInjury OR #BanVaccine OR #VaccineDeaths OR #NoToVacccines"
c.Since = "2019-03-01"
c.until = "2021-03-01"
c.Output = "../../Data/Raw/ids_anti_en.csv"
c.Store_csv = True

# Run
twint.run.Search(c)
