import twint

# Configure
c = twint.Config()
c.Custom["tweet"] = ["id"]
c.Search = "#VacinaNao OR #EuNaoVouTomarVacina OR #VacinaMata OR #NaoVouTomarVacina OR #VacinasNao OR #NaoÀsVacinas OR #ChegaDeVacina OR #VacinasMatam OR #NaoQueroVacina OR #NaoVouTomar OR #ContraVacina OR #VacinasCausamAutismo OR #NaoAVacina OR #NaoTomoVacina OR #ForaVacina"
c.Since = "2019-03-01"
c.until = "2021-03-01"
c.Output = "../../Data/Raw/ids_anti_pt.csv"
c.Store_csv = True

# Run
twint.run.Search(c)
