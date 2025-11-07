from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

loader = TextLoader("blackHole.txt", encoding="utf-8")

docs = loader.load()

TextData = """
A **black hole** is one of the most fascinating and mysterious objects in the universe. It is a region in space where gravity is so strong that nothing—not even light—can escape from it. Black holes are formed when very massive stars collapse under their own gravity at the end of their life cycles. The point at the center of a black hole, where all its mass is concentrated, is called a **singularity**, and it has infinite density. Surrounding the singularity is the **event horizon**, the boundary beyond which nothing can return.

The concept of black holes was first predicted by **Albert Einstein’s theory of general relativity** in 1915. However, the term “black hole” was coined much later by physicist **John Archibald Wheeler** in 1967. For a long time, black holes were only theoretical objects, but over the years, scientists have gathered strong evidence for their existence. One of the most famous discoveries came in 2019, when the **Event Horizon Telescope (EHT)** captured the first-ever image of a black hole in the galaxy M87, confirming many aspects of Einstein’s predictions.

Black holes come in different sizes. **Stellar black holes** are formed from collapsing stars and can be a few times more massive than our Sun. **Supermassive black holes**, on the other hand, lie at the centers of most galaxies—including our Milky Way—and can contain millions or even billions of solar masses. There are also **intermediate** and **primordial black holes**, which are smaller and less understood. Despite their size differences, all black holes share the same basic structure: a singularity and an event horizon.

Black holes are not empty voids; they actively affect their surroundings. As matter falls toward a black hole, it forms an **accretion disk** that heats up and emits intense radiation. This process can make black holes some of the brightest objects in the universe, even though the black holes themselves emit no light. The powerful gravitational pull of a black hole can also bend light around it, a phenomenon known as **gravitational lensing**, allowing astronomers to detect their presence indirectly.

In conclusion, black holes remain one of the greatest mysteries in astrophysics. They challenge our understanding of physics, space, and time. Scientists continue to study them to unlock secrets about the universe’s origin, evolution, and ultimate fate. From being mere mathematical predictions to real cosmic phenomena captured on camera, black holes remind us how vast and intriguing the universe truly is.
"""

# print(docs)

splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator=""
)

result = splitter.split_text(TextData)
# result = splitter.split_documents(docs)
print(result)