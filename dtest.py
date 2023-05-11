import dwave.system
import dimod

ENDPOINT = 'https://cloud.dwavesys.com/sapi' # 5.1.1 で取得した ENDPOINT を記載する
SOLVER = 'hybrid_binary_quadratic_model_version2' # 5.1.1 で取得した SOLVER を記載する
TOKEN = 'DEV-1bd893e0bd0c2bdb86f4d9ddf598e7959a07518c' # 5.1.1 で取得した TOKEN を記載する

sampler = dwave.system.composites.EmbeddingComposite(
    dwave.system.samplers.DWaveSampler(
    endpoint=ENDPOINT,
    token=TOKEN,
    solver=SOLVER
    )
)

'''
h = {0: -1}
J = {(0, 0): -1, (0, 1): 2, (1, 1): -1}
bqm = dimod.BinaryQuadraticModel.from_ising(h, J)

response = sampler.sample(bqm, chain_strength = 3)
response
'''