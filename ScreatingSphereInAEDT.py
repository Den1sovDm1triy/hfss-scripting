import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.NewProject()
oProject.Rename("C:/Users/denisov.dv/Documents/Ansoft/SphereDIffraction.aedt", True)
oProject.InsertDesign("HFSS", "HFSSDesign1", "HFSS Terminal Network", "")
oDesign = oProject.SetActiveDesign("HFSSDesign1")
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.CreateSphere(
	[
		"NAME:SphereParameters",
		"XCenter:="		, "0mm",
		"YCenter:="		, "0mm",
		"ZCenter:="		, "0mm",
		"Radius:="		, "1.0770329614269mm"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Sphere1",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"ShellElement:="	, False,
		"ShellElementThickness:=", "0mm",
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"Sphere1:CreateSphere:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Radius",
					"Value:="		, "15mm"
				]
			]
		]
	])
oProject.Save()
oProject.Save()
oModule = oDesign.GetModule("BoundarySetup")
oModule.AssignPlaneWave(
	[
		"NAME:IncPWave1",
		"IsCartesian:="		, True,
		"EoX:="			, "1",
		"EoY:="			, "0",
		"EoZ:="			, "0",
		"kX:="			, "0",
		"kY:="			, "0",
		"kZ:="			, "1",
		"OriginX:="		, "0mm",
		"OriginY:="		, "0mm",
		"OriginZ:="		, "0mm",
		"IsPropagating:="	, True,
		"IsEvanescent:="	, False,
		"IsEllipticallyPolarized:=", False
	])
oModule = oDesign.GetModule("AnalysisSetup")
oModule.InsertSetup("HfssDriven", 
	[
		"NAME:Setup1",
		"SolveType:="		, "Single",
		"Frequency:="		, "10GHz",
		"MaxDeltaE:="		, 0.1,
		"MaximumPasses:="	, 6,
		"MinimumPasses:="	, 1,
		"MinimumConvergedPasses:=", 1,
		"PercentRefinement:="	, 30,
		"IsEnabled:="		, True,
		[
			"NAME:MeshLink",
			"ImportMesh:="		, False
		],
		"BasisOrder:="		, 1,
		"DoLambdaRefine:="	, True,
		"DoMaterialLambda:="	, True,
		"SetLambdaTarget:="	, False,
		"Target:="		, 0.3333,
		"UseMaxTetIncrease:="	, False,
		"DrivenSolverType:="	, "Direct Solver",
		"EnhancedLowFreqAccuracy:=", False,
		"SaveRadFieldsOnly:="	, False,
		"SaveAnyFields:="	, True,
		"IESolverType:="	, "Auto",
		"LambdaTargetForIESolver:=", 0.15,
		"UseDefaultLambdaTgtForIESolver:=", True,
		"IE Solver Accuracy:="	, "Balanced",
		"InfiniteSphereSetup:="	, ""
	])
oModule = oDesign.GetModule("ModelSetup")
oModule.CreateOpenRegion(
	[
		"NAME:Settings",
		"OpFreq:="		, "10GHz",
		"Boundary:="		, "Radiation",
		"ApplyInfiniteGP:="	, False
	])
oEditor.AssignMaterial(
	[
		"NAME:Selections",
		"AllowRegionDependentPartSelectionForPMLCreation:=", True,
		"AllowRegionSelectionForPMLCreation:=", True,
		"Selections:="		, "Sphere1"
	], 
	[
		"NAME:Attributes",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False,
		"ShellElement:="	, False,
		"ShellElementThickness:=", "nan ",
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])
oProject.Save()
oDesign.AnalyzeAll()
oModule = oDesign.GetModule("FieldsReporter")
oModule.CreateFieldPlot(
	[
		"NAME:Mag_E1",
		"SolutionName:="	, "Setup1 : LastAdaptive",
		"UserSpecifyName:="	, 0,
		"UserSpecifyFolder:="	, 0,
		"QuantityName:="	, "Mag_E",
		"PlotFolder:="		, "E Field",
		"StreamlinePlot:="	, False,
		"AdjacentSidePlot:="	, False,
		"FullModelPlot:="	, False,
		"IntrinsicVar:="	, "Freq=\'10GHz\' Phase=\'0deg\'",
		"PlotGeomInfo:="	, [1,"Surface","CutPlane",1,"Global:YZ"],
		"FilterBoxes:="		, [0],
		[
			"NAME:PlotOnSurfaceSettings",
			"Filled:="		, False,
			"IsoValType:="		, "Fringe",
			"AddGrid:="		, False,
			"MapTransparency:="	, True,
			"Refinement:="		, 0,
			"Transparency:="	, 0,
			"SmoothingLevel:="	, 0,
			"ShadingType:="		, 0,
			[
				"NAME:Arrow3DSpacingSettings",
				"ArrowUniform:="	, True,
				"ArrowSpacing:="	, 0,
				"MinArrowSpacing:="	, 0,
				"MaxArrowSpacing:="	, 0
			],
			"GridColor:="		, [255,255,255]
		],
		"EnableGaussianSmoothing:=", False,
		"SurfaceOnly:="		, False
	], "Field")
oProject.Save()
