plugins { kotlin("multiplatform") version "2.2.21" }
kotlin {
    js(IR) {
        outputModuleName.set("joetopia-engine")
        browser {
            webpackTask { mainOutputFileName.set("joetopia-engine.js"); output.library = "JoetopiaKt"; output.libraryTarget = "var" }
            testTask { enabled = false }
        }
        binaries.executable()
    }
}
