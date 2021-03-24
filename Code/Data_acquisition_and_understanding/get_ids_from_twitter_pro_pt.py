import twint

# Configure
c = twint.Config()
c.Custom["tweet"] = ["id"]
c.Search = "#VacinaParaTodosJa OR #VacinaParaTodos OR #VacinaSim OR #VacinaJa OR #VemVacina OR #VacinaSalva OR #TodosPelasVacinas OR #VacinaFunciona OR #VacinaÉAmorAoPróximo OR #VacinaAgora OR #QueroSerVacinado OR #QueroSerVacinada OR #ExijoVacina OR #VivaAVacina OR #QueroVacina OR #VacinasFuncionam OR #ProVacina OR #VacinasPelaVida OR #VacinasSalvamVidas OR #Vacinese OR #EuQueroVacina OR #EuQueroVacina OR #VacinasSalvam OR #VacinasJa OR #VacinasFuncionam"
c.Since = "2019-03-01"
c.until = "2021-03-01"
c.Output = "../../Data/Raw/ids_pro_pt.csv"
c.Store_csv = True

# Run
twint.run.Search(c)
