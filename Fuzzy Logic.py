import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

pendapatan = ctrl.Antecedent(np.arange(0, 3, 1), 'pendapatan')
hutang = ctrl.Antecedent(np.arange(0, 100, 1), 'hutang')
BLT = ctrl.Consequent(np.arange(0, 3, 1), 'BLT')

pendapatan['rendah'] = fuzz.trimf(pendapatan.universe, [0, 0, 1])
pendapatan['sedang'] = fuzz.trimf(pendapatan.universe, [0, 1, 2])
pendapatan['tinggi'] = fuzz.trimf(pendapatan.universe, [1, 2, 2])

hutang['rendah'] = fuzz.trimf(hutang.universe, [0, 0, 49])
hutang['sedang'] = fuzz.trimf(hutang.universe, [0, 49, 98])
hutang['tinggi'] = fuzz.trimf(hutang.universe, [49, 98, 98])

BLT['tidak_layak'] = fuzz.trimf(BLT.universe, [0, 0, 0.5])
BLT['layak'] = fuzz.trimf(BLT.universe, [0.5, 1, 1])

rule1 = ctrl.Rule(pendapatan['rendah'] & hutang['rendah'], BLT['layak'])
rule2 = ctrl.Rule(pendapatan['rendah'] & hutang['sedang'], BLT['layak'])
rule3 = ctrl.Rule(pendapatan['rendah'] & hutang['tinggi'], BLT['layak'])
rule4 = ctrl.Rule(pendapatan['sedang'] & hutang['rendah'], BLT['tidak_layak'])
rule5 = ctrl.Rule(pendapatan['sedang'] & hutang['sedang'], BLT['tidak_layak'])
rule6 = ctrl.Rule(pendapatan['sedang'] & hutang['tinggi'], BLT['layak'])
rule7 = ctrl.Rule(pendapatan['tinggi'] & hutang['rendah'], BLT['tidak_layak'])
rule8 = ctrl.Rule(pendapatan['tinggi'] & hutang['sedang'], BLT['tidak_layak'])
rule9 = ctrl.Rule(pendapatan['tinggi'] & hutang['tinggi'], BLT['tidak_layak'])

tipping_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])

tipping = ctrl.ControlSystemSimulation(tipping_ctrl)

tipping.input['pendapatan'] = 1.273
tipping.input['hutang'] = 80.701

tipping.compute()

print (tipping.output['BLT'])


