from datetime import date
from decimal import Decimal
from typing import List, Optional

from sqlalchemy import Boolean, Column, Date, Double, Enum, ForeignKeyConstraint, Integer, Numeric, PrimaryKeyConstraint, String
from sqlmodel import Field, Relationship, SQLModel

class Feeds(SQLModel, table=True):
    __table_args__ = (
        PrimaryKeyConstraint('id', name='feeds_pkey'),
    )

    id: Optional[int] = Field(default=None, sa_column=Column('id', Integer, primary_key=True))
    cereal_type: Optional[str] = Field(default=None, sa_column=Column('cereal_type', Enum('corn', 'wheat', 'barley', 'set-aside', 'bought-in forage', 'minerals', 'concentrates', 'milk replacer', 'oils', name='cereal_type_t')))
    dry_matter: Optional[float] = Field(default=None, sa_column=Column('dry_matter', Double(53)))
    xp: Optional[float] = Field(default=None, sa_column=Column('xp', Double(53)))
    energy: Optional[float] = Field(default=None, sa_column=Column('energy', Double(53)))

    feed_ration: List['FeedRation'] = Relationship(back_populates='feeds')


class GeneralFarm(SQLModel, table=True):
    __tablename__ = 'general_farm'
    __table_args__ = (
        PrimaryKeyConstraint('general_id', name='general_farm_pkey'),
    )

    general_id: Optional[int] = Field(default=None, sa_column=Column('general_id', Integer, primary_key=True))
    username: Optional[str] = Field(default=None, sa_column=Column('username', String(25)))
    email: Optional[str] = Field(default=None, sa_column=Column('email', String(50)))
    password: Optional[str] = Field(default=None, sa_column=Column('password', String(255)))
    land: Optional[str] = Field(default=None, sa_column=Column('land', String(30)))
    region: Optional[str] = Field(default=None, sa_column=Column('region', String(50)))
    currency: Optional[str] = Field(default=None, sa_column=Column('currency', String(20)))
    legal_status: Optional[str] = Field(default=None, sa_column=Column('legal status', String(50)))
    reference_year_data: Optional[int] = Field(default=None, sa_column=Column('reference_year_data', Integer))
    cash_crop: Optional[bool] = Field(default=None, sa_column=Column('cash_crop', Boolean))
    sows: Optional[bool] = Field(default=None, sa_column=Column('sows', Boolean))
    pig_finishing: Optional[bool] = Field(default=None, sa_column=Column('pig_finishing', Boolean))
    year: Optional[int] = Field(default=None, sa_column=Column('year', Integer))

    acerage_prices: List['AceragePrices'] = Relationship(back_populates='general')
    direct_aid_from_farm: List['DirectAidFromFarm'] = Relationship(back_populates='general')
    feed_prices_dry_matter: List['FeedPricesDryMatter'] = Relationship(back_populates='general')
    feed_ration: List['FeedRation'] = Relationship(back_populates='general')
    feeding_finishing: List['FeedingFinishing'] = Relationship(back_populates='general')
    fertilizer: List['Fertilizer'] = Relationship(back_populates='general')
    fix_costs: List['FixCosts'] = Relationship(back_populates='general')
    labor_alloc_sow_finishing: List['LaborAllocSowFinishing'] = Relationship(back_populates='general')
    liabilities_interest_rates: List['LiabilitiesInterestRates'] = Relationship(back_populates='general')
    overhead_costs: List['OverheadCosts'] = Relationship(back_populates='general')
    performance_pig_finishing: List['PerformancePigFinishing'] = Relationship(back_populates='general')
    pig_finishing_: List['PigFinishing'] = Relationship(back_populates='general')
    prices_finishing: List['PricesFinishing'] = Relationship(back_populates='general')
    prices_sows: List['PricesSows'] = Relationship(back_populates='general')
    sales_weight: List['SalesWeight'] = Relationship(back_populates='general')
    sows_: List['Sows'] = Relationship(back_populates='general')
    sows_performance: List['SowsPerformance'] = Relationship(back_populates='general')
    var_cost_finishing: List['VarCostFinishing'] = Relationship(back_populates='general')
    variable_costs_sows: List['VariableCostsSows'] = Relationship(back_populates='general')
    buildings: List['Buildings'] = Relationship(back_populates='general')
    feed_sows: List['FeedSows'] = Relationship(back_populates='general')
    labour: List['Labour'] = Relationship(back_populates='general')
    machines: List['Machines'] = Relationship(back_populates='general')
    cash_crops: List['CashCrops'] = Relationship(back_populates='general')
    land_use: List['LandUse'] = Relationship(back_populates='general')
    var_cost_crop: List['VarCostCrop'] = Relationship(back_populates='general')


class AceragePrices(SQLModel, table=True):
    __tablename__ = 'acerage_prices'
    __table_args__ = (
        ForeignKeyConstraint(['general_id'], ['general_farm.general_id'], name='acerage_prices_general_id_fkey'),
        PrimaryKeyConstraint('acerage_id', name='acerage_prices_pkey')
    )

    acerage_id: Optional[int] = Field(default=None, sa_column=Column('acerage_id', Integer, primary_key=True))
    land_type: Optional[str] = Field(default=None, sa_column=Column('land_type', String(50), comment='Cropland\tGrassland\tOther incl. wood'))
    own_land: Optional[Decimal] = Field(default=None, sa_column=Column('own_land', Numeric, comment='ha'))
    rented_land: Optional[Decimal] = Field(default=None, sa_column=Column('rented_land', Numeric, comment='ha'))
    rent_existing_contracts: Optional[Decimal] = Field(default=None, sa_column=Column('rent_existing_contracts', Numeric, comment='C/ha'))
    rent_new_contracts: Optional[Decimal] = Field(default=None, sa_column=Column('rent_new_contracts', Numeric, comment='C/ha'))
    market_value: Optional[Decimal] = Field(default=None, sa_column=Column('market_value', Numeric, comment='C/ha'))
    general_id: Optional[int] = Field(default=None, sa_column=Column('general_id', Integer))
    year: Optional[int] = Field(default=None, sa_column=Column('year', Integer))

    general: Optional['GeneralFarm'] = Relationship(back_populates='acerage_prices')


class DirectAidFromFarm(SQLModel, table=True):
    __tablename__ = 'direct_aid_from_farm'
    __table_args__ = (
        ForeignKeyConstraint(['general_id'], ['general_farm.general_id'], name='direct_aid_from_farm_general_id_fkey'),
        PrimaryKeyConstraint('direct_aid_id', name='direct_aid_from_farm_pkey')
    )

    direct_aid_id: Optional[int] = Field(default=None, sa_column=Column('direct_aid_id', Integer, primary_key=True))
    compensatory_allovance_disadvantage_area: Optional[Decimal] = Field(default=None, sa_column=Column('compensatory_allovance_disadvantage_area', Numeric, comment='C/year'))
    general_id: Optional[int] = Field(default=None, sa_column=Column('general_id', Integer))
    year: Optional[int] = Field(default=None, sa_column=Column('year', Integer))

    general: Optional['GeneralFarm'] = Relationship(back_populates='direct_aid_from_farm')


class FeedPricesDryMatter(SQLModel, table=True):
    __tablename__ = 'feed_prices_dry_matter'
    __table_args__ = (
        ForeignKeyConstraint(['general_id'], ['general_farm.general_id'], name='feed_prices_dry_matter_general_id_fkey'),
        PrimaryKeyConstraint('feed_prices_id', name='feed_prices_dry_matter_pkey')
    )

    feed_prices_id: Optional[int] = Field(default=None, sa_column=Column('feed_prices_id', Integer, primary_key=True))
    feed_type: Optional[str] = Field(default=None, sa_column=Column('feed_type', String(50), comment='Bought-in forage, Minerals, Concentrates, Milk replacer ,Oils, Finishing Feed I, Finishing Feed II, Finishing , Feed III, Finishing Feed IV, Gestation feed, Lactation feed, Special gilt feed, Special boar feed, Piglet feed I, Piglet feed II'))
    price_per_tonne: Optional[Decimal] = Field(default=None, sa_column=Column('price_per_tonne', Numeric, comment='C/t'))
    dry_matter_percent: Optional[Decimal] = Field(default=None, sa_column=Column('dry_matter_percent', Numeric(5, 4), comment='%'))
    energy_mj: Optional[Decimal] = Field(default=None, sa_column=Column('energy_mj', Numeric))
    protein: Optional[Decimal] = Field(default=None, sa_column=Column('protein', Numeric, comment='%'))
    text: Optional[str] = Field(default=None, sa_column=Column('text', String(255)))
    concentrate: Optional[bool] = Field(default=None, sa_column=Column('concentrate', Boolean))
    general_id: Optional[int] = Field(default=None, sa_column=Column('general_id', Integer))
    year: Optional[int] = Field(default=None, sa_column=Column('year', Integer))

    general: Optional['GeneralFarm'] = Relationship(back_populates='feed_prices_dry_matter')


class FeedRation(SQLModel, table=True):
    __tablename__ = 'feed_ration'
    __table_args__ = (
        ForeignKeyConstraint(['feeds_id'], ['feeds.id'], name='feed_ration_feeds_id_fkey'),
        ForeignKeyConstraint(['general_id'], ['general_farm.general_id'], name='feed_ration_general_id_fkey'),
        PrimaryKeyConstraint('feed_ration_id', name='feed_ration_pkey')
    )

    feed_ration_id: Optional[int] = Field(default=None, sa_column=Column('feed_ration_id', Integer, primary_key=True))
    production: Optional[str] = Field(default=None, sa_column=Column('production', Enum('sows', 'finishing', name='production_t')))
    feed_sources: Optional[str] = Field(default=None, sa_column=Column('feed_sources', Enum('Self produced', 'Bought feed', name='feed_sources_t')))
    feed_type: Optional[str] = Field(default=None, sa_column=Column('feed_type', Enum('Gestation feed', 'Lactation feed', 'Special gilt feed', 'Special boar feed', 'Piglet feed 1', 'Piglet feed 2', 'Finishing feed 1', 'Finishing feed 2', 'Finishing feed 3', name='feed_type_t')))
    feed_share: Optional[Decimal] = Field(default=None, sa_column=Column('feed_share', Numeric))
    total_amount_feed_used: Optional[Decimal] = Field(default=None, sa_column=Column('total_amount_feed_used', Numeric))
    general_id: Optional[int] = Field(default=None, sa_column=Column('general_id', Integer))
    year: Optional[int] = Field(default=None, sa_column=Column('year', Integer))
    feeds_id: Optional[int] = Field(default=None, sa_column=Column('feeds_id', Integer))

    feeds: Optional['Feeds'] = Relationship(back_populates='feed_ration')
    general: Optional['GeneralFarm'] = Relationship(back_populates='feed_ration')


class FeedingFinishing(SQLModel, table=True):
    __tablename__ = 'feeding_finishing'
    __table_args__ = (
        ForeignKeyConstraint(['general_id'], ['general_farm.general_id'], name='feeding_finishing_general_id_fkey'),
        PrimaryKeyConstraint('feed_fin_id', name='feeding_finishing_pkey')
    )

    feed_fin_id: Optional[int] = Field(default=None, sa_column=Column('feed_fin_id', Integer, primary_key=True))
    proportion_finishing_feed_1: Optional[Decimal] = Field(default=None, sa_column=Column('proportion_finishing_feed_1', Numeric(5, 4), comment='%'))
    proportion_finishing_feed_2: Optional[Decimal] = Field(default=None, sa_column=Column('proportion_finishing_feed_2', Numeric(5, 4), comment='%'))
    proportion_finishing_feed_3: Optional[Decimal] = Field(default=None, sa_column=Column('proportion_finishing_feed_3', Numeric(5, 4)))
    amount_finishing_feed_1: Optional[Decimal] = Field(default=None, sa_column=Column('amount_finishing_feed_1', Numeric, comment='kg/year'))
    amount_finishing_feed_2: Optional[Decimal] = Field(default=None, sa_column=Column('amount_finishing_feed_2', Numeric, comment='kg/year'))
    amount_finishing_feed_3: Optional[Decimal] = Field(default=None, sa_column=Column('amount_finishing_feed_3', Numeric, comment='kg/year'))
    total_amount_feed: Optional[Decimal] = Field(default=None, sa_column=Column('total_amount_feed', Numeric, comment='kg/year'))
    general_id: Optional[int] = Field(default=None, sa_column=Column('general_id', Integer))
    year: Optional[int] = Field(default=None, sa_column=Column('year', Integer))

    general: Optional['GeneralFarm'] = Relationship(back_populates='feeding_finishing')


class Fertilizer(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['general_id'], ['general_farm.general_id'], name='fertilizer_general_id_fkey'),
        PrimaryKeyConstraint('fertilizer_id', name='fertilizer_pkey')
    )

    fertilizer_id: Optional[int] = Field(default=None, sa_column=Column('fertilizer_id', Integer, primary_key=True))
    fertilizer_type: Optional[str] = Field(default=None, sa_column=Column('fertilizer_type', Enum('organic', 'mineral', name='fertilizer_type_t')))
    fertilizer_name: Optional[str] = Field(default=None, sa_column=Column('fertilizer_name', Enum('nitrogen', 'phosphorus', 'potash', 'calcium', 'others', name='fertilizer_name_t')))
    fertilizer_name_custom: Optional[str] = Field(default=None, sa_column=Column('fertilizer_name_custom', String(255)))
    amount: Optional[Decimal] = Field(default=None, sa_column=Column('amount', Numeric))
    amount_unit: Optional[Decimal] = Field(default=None, sa_column=Column('amount_unit', Numeric))
    n_content_per_unit: Optional[Decimal] = Field(default=None, sa_column=Column('n_content_per_unit', Numeric))
    general_id: Optional[int] = Field(default=None, sa_column=Column('general_id', Integer))
    year: Optional[int] = Field(default=None, sa_column=Column('year', Integer))

    general: Optional['GeneralFarm'] = Relationship(back_populates='fertilizer')


class FixCosts(SQLModel, table=True):
    __tablename__ = 'fix_costs'
    __table_args__ = (
        ForeignKeyConstraint(['general_id'], ['general_farm.general_id'], name='fix_costs_general_id_fkey'),
        PrimaryKeyConstraint('fix_cost_id', name='fix_costs_pkey')
    )

    fix_cost_id: Optional[int] = Field(default=None, sa_column=Column('fix_cost_id', Integer, primary_key=True))
    feed_grinding_preparation: Optional[Decimal] = Field(default=None, sa_column=Column('feed_grinding_preparation', Numeric, comment='C/enterprise'))
    insurance: Optional[Decimal] = Field(default=None, sa_column=Column('insurance', Numeric, comment='C/enterprise'))
    cleaning: Optional[Decimal] = Field(default=None, sa_column=Column('cleaning', Numeric, comment='C/enterprise'))
    others: Optional[Decimal] = Field(default=None, sa_column=Column('others', Numeric, comment='C/enterprise'))
    general_id: Optional[int] = Field(default=None, sa_column=Column('general_id', Integer))
    year: Optional[int] = Field(default=None, sa_column=Column('year', Integer))

    general: Optional['GeneralFarm'] = Relationship(back_populates='fix_costs')


class LaborAllocSowFinishing(SQLModel, table=True):
    __tablename__ = 'labor_alloc_sow_finishing'
    __table_args__ = (
        ForeignKeyConstraint(['general_id'], ['general_farm.general_id'], name='labor_alloc_sow_finishing_general_id_fkey'),
        PrimaryKeyConstraint('id', name='labor_alloc_sow_finishing_pkey')
    )

    id: Optional[int] = Field(default=None, sa_column=Column('id', Integer, primary_key=True))
    casual_labor_sow: Optional[Decimal] = Field(default=None, sa_column=Column('casual_labor_sow', Numeric, comment='0,0x'))
    family_labor_sow: Optional[Decimal] = Field(default=None, sa_column=Column('family_labor_sow', Numeric, comment='0,0x'))
    casual_labor_finishing: Optional[Decimal] = Field(default=None, sa_column=Column('casual_labor_finishing', Numeric, comment='0,0x'))
    family_labor_finishing: Optional[Decimal] = Field(default=None, sa_column=Column('family_labor_finishing', Numeric, comment='0,0x'))
    general_id: Optional[int] = Field(default=None, sa_column=Column('general_id', Integer))
    year: Optional[int] = Field(default=None, sa_column=Column('year', Integer))

    general: Optional['GeneralFarm'] = Relationship(back_populates='labor_alloc_sow_finishing')


class LiabilitiesInterestRates(SQLModel, table=True):
    __tablename__ = 'liabilities_interest_rates'
    __table_args__ = (
        ForeignKeyConstraint(['general_id'], ['general_farm.general_id'], name='liabilities_interest_rates_general_id_fkey'),
        PrimaryKeyConstraint('liabilities_id', name='liabilities_interest_rates_pkey')
    )

    liabilities_id: Optional[int] = Field(default=None, sa_column=Column('liabilities_id', Integer, primary_key=True))
    long_term_loans: Optional[Decimal] = Field(default=None, sa_column=Column('long_term_loans', Numeric(5, 4), comment='%'))
    medium_term_loans: Optional[Decimal] = Field(default=None, sa_column=Column('medium_term_loans', Numeric(5, 4), comment='%'))
    short_term_loans: Optional[Decimal] = Field(default=None, sa_column=Column('short_term_loans', Numeric(5, 4), comment='%'))
    circulating_capital_overdraft: Optional[Decimal] = Field(default=None, sa_column=Column('circulating_capital_overdraft', Numeric(5, 4), comment='%'))
    savings: Optional[Decimal] = Field(default=None, sa_column=Column('savings', Numeric(5, 4), comment='%'))
    total_liabilities: Optional[Decimal] = Field(default=None, sa_column=Column('total_liabilities', Numeric, comment='C'))
    total_long_term_loans: Optional[Decimal] = Field(default=None, sa_column=Column('total_long_term_loans', Numeric, comment='C'))
    total_medium_term_loans: Optional[Decimal] = Field(default=None, sa_column=Column('total_medium_term_loans', Numeric, comment='C'))
    total_short_term_loans: Optional[Decimal] = Field(default=None, sa_column=Column('total_short_term_loans', Numeric, comment='C'))
    perc_debt_total_assets: Optional[Decimal] = Field(default=None, sa_column=Column('perc_debt_total_assets', Numeric(5, 4), comment='%'))
    general_id: Optional[int] = Field(default=None, sa_column=Column('general_id', Integer))
    year: Optional[int] = Field(default=None, sa_column=Column('year', Integer))

    general: Optional['GeneralFarm'] = Relationship(back_populates='liabilities_interest_rates')


class OverheadCosts(SQLModel, table=True):
    __tablename__ = 'overhead_costs'
    __table_args__ = (
        ForeignKeyConstraint(['general_id'], ['general_farm.general_id'], name='overhead_costs_general_id_fkey'),
        PrimaryKeyConstraint('overhead_id', name='overhead_costs_pkey')
    )

    overhead_id: Optional[int] = Field(default=None, sa_column=Column('overhead_id', Integer, primary_key=True))
    land_improvements: Optional[Decimal] = Field(default=None, sa_column=Column('land_improvements', Numeric, comment='Drainage etc.;C/year'))
    maintenance_machinery: Optional[Decimal] = Field(default=None, sa_column=Column('maintenance_machinery', Numeric, comment='If not known, calculate proxy, e.g. 3 % of the purchase price per annum; avoid double counting!;C/year'))
    maintenance_buildings: Optional[Decimal] = Field(default=None, sa_column=Column('maintenance_buildings', Numeric, comment='If not known, calculate proxy, e.g. 1,5 % of the purchase price per annum; avoid double counting!;C/year'))
    contracted_labour_machinery_association: Optional[Decimal] = Field(default=None, sa_column=Column('contracted_labour_machinery_association', Numeric, comment='C/year'))
    diesel_vehicles: Optional[Decimal] = Field(default=None, sa_column=Column('diesel_vehicles', Numeric, comment='Includes Pick-up trucks, farm vehicles, NOT tractors for crop and forage production (var. cost per ha!);C/year'))
    diesel_heating_irrigation: Optional[Decimal] = Field(default=None, sa_column=Column('diesel_heating_irrigation', Numeric, comment='C/year'))
    gasoline: Optional[Decimal] = Field(default=None, sa_column=Column('gasoline', Numeric, comment='C/year'))
    gas: Optional[Decimal] = Field(default=None, sa_column=Column('gas', Numeric, comment='C/year'))
    electricity: Optional[Decimal] = Field(default=None, sa_column=Column('electricity', Numeric, comment='C/year'))
    water_fresh_waste_water_fees: Optional[Decimal] = Field(default=None, sa_column=Column('water_fresh_waste_water_fees', Numeric, comment='Water and energy for the farmstead, not for crop production and other enterprises\t;C/year'))
    farm_insurance: Optional[Decimal] = Field(default=None, sa_column=Column('farm_insurance', Numeric, comment='Insurances to cover the farm, e.g. fire insurance, crop insurance under other variable cost crop;C/year'))
    invalidity_insurance: Optional[Decimal] = Field(default=None, sa_column=Column('invalidity_insurance', Numeric, comment='Fees for institutions that provide accident insurances and check safety on the farms;C/year\t'))
    taxes_fees: Optional[Decimal] = Field(default=None, sa_column=Column('taxes_fees', Numeric, comment='Only farm taxes like ground tax, no personal taxes like income tax!;C/year'))
    advisory_services_trainings: Optional[Decimal] = Field(default=None, sa_column=Column('advisory_services_trainings', Numeric, comment='Costs for advisory/extension services if it cannot be allocated to the enterprises;C/year'))
    accounting: Optional[Decimal] = Field(default=None, sa_column=Column('accounting', Numeric, comment='E.g. costs for hiring a person or a company to do the accounting;C/year'))
    office_communication_subs: Optional[Decimal] = Field(default=None, sa_column=Column('office_communication_subs', Numeric, comment='All kind of materials, hardware and communication expenses;C/year\t\t'))
    others: Optional[Decimal] = Field(default=None, sa_column=Column('others', Numeric, comment='C/year'))
    general_id: Optional[int] = Field(default=None, sa_column=Column('general_id', Integer))
    year: Optional[int] = Field(default=None, sa_column=Column('year', Integer))

    general: Optional['GeneralFarm'] = Relationship(back_populates='overhead_costs')


class PerformancePigFinishing(SQLModel, table=True):
    __tablename__ = 'performance_pig_finishing'
    __table_args__ = (
        ForeignKeyConstraint(['general_id'], ['general_farm.general_id'], name='performance_pig_finishing_general_id_fkey'),
        PrimaryKeyConstraint('performance_fin_id', name='performance_pig_finishing_pkey')
    )

    performance_fin_id: Optional[int] = Field(default=None, sa_column=Column('performance_fin_id', Integer, primary_key=True))
    stalling_in_weight: Optional[Decimal] = Field(default=None, sa_column=Column('stalling_in_weight', Numeric, comment='kg LW per head'))
    stalling_in_weight_em_ic_piglets: Optional[Decimal] = Field(default=None, sa_column=Column('stalling_in_weight_em_ic_piglets', Numeric, comment='kg LW per head'))
    avg_duration_finishing_period: Optional[Decimal] = Field(default=None, sa_column=Column('avg_duration_finishing_period', Numeric, comment='days'))
    cleaning_days_cycle: Optional[Decimal] = Field(default=None, sa_column=Column('cleaning_days_cycle', Numeric, comment='days'))
    days_without_animals_instable: Optional[Decimal] = Field(default=None, sa_column=Column('days_without_animals_instable', Numeric, comment='days'))
    mortality: Optional[Decimal] = Field(default=None, sa_column=Column('mortality', Numeric(5, 4), comment='%'))
    avg_selling_weight_gi_ba: Optional[Decimal] = Field(default=None, sa_column=Column('avg_selling_weight_gi_ba', Numeric, comment='kg LW per head'))
    carcass_yield_gi_ba: Optional[Decimal] = Field(default=None, sa_column=Column('carcass_yield_gi_ba', Numeric))
    lean_meat_fom_gi_ba: Optional[Decimal] = Field(default=None, sa_column=Column('lean_meat_fom_gi_ba', Numeric, comment='%'))
    index_points_autofom_gi_ba: Optional[Decimal] = Field(default=None, sa_column=Column('index_points_autofom_gi_ba', Numeric, comment='0,0x'))
    avg_selling_weight_em_ic: Optional[Decimal] = Field(default=None, sa_column=Column('avg_selling_weight_em_ic', Numeric, comment='kg LW per head'))
    carcass_yield_em_ic: Optional[Decimal] = Field(default=None, sa_column=Column('carcass_yield_em_ic', Numeric(5, 4), comment='%'))
    index_points_autofom_em_ic: Optional[Decimal] = Field(default=None, sa_column=Column('index_points_autofom_em_ic', Numeric, comment='0,0x'))
    avg_duration_finishing_period_em_ic: Optional[Decimal] = Field(default=None, sa_column=Column('avg_duration_finishing_period_em_ic', Numeric, comment='0,0x'))
    general_id: Optional[int] = Field(default=None, sa_column=Column('general_id', Integer))
    year: Optional[int] = Field(default=None, sa_column=Column('year', Integer))

    general: Optional['GeneralFarm'] = Relationship(back_populates='performance_pig_finishing')


class PigFinishing(SQLModel, table=True):
    __tablename__ = 'pig_finishing'
    __table_args__ = (
        ForeignKeyConstraint(['general_id'], ['general_farm.general_id'], name='pig_finishing_general_id_fkey'),
        PrimaryKeyConstraint('finishing_id', name='pig_finishing_pkey')
    )

    finishing_id: int = Field(sa_column=Column('finishing_id', Integer, primary_key=True))
    general_id: Optional[int] = Field(default=None, sa_column=Column('general_id', Integer))
    production_system: Optional[str] = Field(default=None, sa_column=Column('production_system', Enum('normal pig finishing', 'additional boar finishing', name='production_system_t')))
    production_cyle: Optional[str] = Field(default=None, sa_column=Column('production_cyle', Enum('all-in all-out by barn', 'continuous system', name='production_cyle_t')))
    animal_places: Optional[int] = Field(default=None, sa_column=Column('animal_places', Integer, comment='No. heads'))
    no_sold_pigs_gi_ba: Optional[int] = Field(default=None, sa_column=Column('no_sold_pigs_gi_ba', Integer, comment='No heads'))
    no_sold_em_ic: Optional[int] = Field(default=None, sa_column=Column('no_sold_em_ic', Integer))
    share_gi_pigs: Optional[Decimal] = Field(default=None, sa_column=Column('share_gi_pigs', Numeric(5, 4), comment='%'))
    year: Optional[int] = Field(default=None, sa_column=Column('year', Integer))

    general: Optional['GeneralFarm'] = Relationship(back_populates='pig_finishing_')
    buildings: List['Buildings'] = Relationship(back_populates='finishing')
    feed_sows: List['FeedSows'] = Relationship(back_populates='finishing')
    labour: List['Labour'] = Relationship(back_populates='finishing')
    machines: List['Machines'] = Relationship(back_populates='finishing')


class PricesFinishing(SQLModel, table=True):
    __tablename__ = 'prices_finishing'
    __table_args__ = (
        ForeignKeyConstraint(['general_id'], ['general_farm.general_id'], name='prices_finishing_general_id_fkey'),
        PrimaryKeyConstraint('prices_fin_id', name='prices_finishing_pkey')
    )

    prices_fin_id: Optional[int] = Field(default=None, sa_column=Column('prices_fin_id', Integer, primary_key=True))
    buying_f_castpiglets: Optional[Decimal] = Field(default=None, sa_column=Column('buying_f_castpiglets', Numeric, comment='C/ kg LW'))
    buying_piglets_for_finishing: Optional[Decimal] = Field(default=None, sa_column=Column('buying_piglets_for_finishing', Numeric, comment='C/ kg LW'))
    selling_finishing_pigs_gi_ba: Optional[Decimal] = Field(default=None, sa_column=Column('selling_finishing_pigs_gi_ba', Numeric, comment='C/ kg CW'))
    selling_finishing_pigs_em_ic: Optional[Decimal] = Field(default=None, sa_column=Column('selling_finishing_pigs_em_ic', Numeric, comment='C/ kg CW'))
    general_id: Optional[int] = Field(default=None, sa_column=Column('general_id', Integer))
    year: Optional[int] = Field(default=None, sa_column=Column('year', Integer))

    general: Optional['GeneralFarm'] = Relationship(back_populates='prices_finishing')


class PricesSows(SQLModel, table=True):
    __tablename__ = 'prices_sows'
    __table_args__ = (
        ForeignKeyConstraint(['general_id'], ['general_farm.general_id'], name='prices_sows_general_id_fkey'),
        PrimaryKeyConstraint('prices_sows_id', name='prices_sows_pkey')
    )

    prices_sows_id: Optional[int] = Field(default=None, sa_column=Column('prices_sows_id', Integer, primary_key=True))
    buying_gilts: Optional[Decimal] = Field(default=None, sa_column=Column('buying_gilts', Numeric, comment='C/head'))
    buying_boars: Optional[Decimal] = Field(default=None, sa_column=Column('buying_boars', Numeric, comment='C/head'))
    selling_sow: Optional[Decimal] = Field(default=None, sa_column=Column('selling_sow', Numeric, comment='C/kg CW'))
    selling_boar: Optional[Decimal] = Field(default=None, sa_column=Column('selling_boar', Numeric, comment='C/kg CW'))
    selling_weaning_piglet: Optional[Decimal] = Field(default=None, sa_column=Column('selling_weaning_piglet', Numeric, comment='C/head'))
    selling_rearing_piglet: Optional[Decimal] = Field(default=None, sa_column=Column('selling_rearing_piglet', Numeric, comment='C/head'))
    proportion_weaned_pigs_sold: Optional[Decimal] = Field(default=None, sa_column=Column('proportion_weaned_pigs_sold', Numeric, comment='% 0,0x'))
    no_weaned_pigs_sold: Optional[Decimal] = Field(default=None, sa_column=Column('no_weaned_pigs_sold', Numeric))
    general_id: Optional[int] = Field(default=None, sa_column=Column('general_id', Integer))
    year: Optional[int] = Field(default=None, sa_column=Column('year', Integer))

    general: Optional['GeneralFarm'] = Relationship(back_populates='prices_sows')


class SalesWeight(SQLModel, table=True):
    __tablename__ = 'sales_weight'
    __table_args__ = (
        ForeignKeyConstraint(['general_id'], ['general_farm.general_id'], name='sales_weight_general_id_fkey'),
        PrimaryKeyConstraint('sales_weight_id', name='sales_weight_pkey')
    )

    sales_weight_id: Optional[int] = Field(default=None, sa_column=Column('sales_weight_id', Integer, primary_key=True))
    sows: Optional[Decimal] = Field(default=None, sa_column=Column('sows', Numeric, comment='kg CW per head'))
    boars: Optional[Decimal] = Field(default=None, sa_column=Column('boars', Numeric, comment='kg CW per head'))
    weaning_piglet: Optional[Decimal] = Field(default=None, sa_column=Column('weaning_piglet', Numeric, comment='kg LW per head'))
    rearing_piglet: Optional[Decimal] = Field(default=None, sa_column=Column('rearing_piglet', Numeric, comment='kg LW per head'))
    general_id: Optional[int] = Field(default=None, sa_column=Column('general_id', Integer))
    year: Optional[int] = Field(default=None, sa_column=Column('year', Integer))

    general: Optional['GeneralFarm'] = Relationship(back_populates='sales_weight')


class Sows(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['general_id'], ['general_farm.general_id'], name='sows_general_id_fkey'),
        PrimaryKeyConstraint('sows_id', name='sows_pkey')
    )

    sows_id: Optional[int] = Field(default=None, sa_column=Column('sows_id', Integer, primary_key=True))
    general_id: Optional[int] = Field(default=None, sa_column=Column('general_id', Integer))
    productionsystem: Optional[str] = Field(default=None, sa_column=Column('productionsystem', Enum('system piglet sales (approx. 8kg)', 'weaner sales (approx. 25-30kg)', 'pure piglet rearing', 'closed system', name='productionsystem_t')))
    production_rhythm: Optional[str] = Field(default=None, sa_column=Column('production_rhythm', Enum('1-week rhythm', '2-week rhythm', '3-week rhythm', '4-week rhythm', 'none or other rhythm', name='production_rhythm_t')))
    no_sows_mated_gilts: Optional[int] = Field(default=None, sa_column=Column('no_sows_mated_gilts', Integer, comment='No. heads'))
    no_unserved_gilts: Optional[int] = Field(default=None, sa_column=Column('no_unserved_gilts', Integer, comment='No. heads'))
    no_boars: Optional[int] = Field(default=None, sa_column=Column('no_boars', Integer, comment='No. heads'))
    total_no_sows_gilts: Optional[int] = Field(default=None, sa_column=Column('total_no_sows_gilts', Integer))
    year: Optional[int] = Field(default=None, sa_column=Column('year', Integer))

    general: Optional['GeneralFarm'] = Relationship(back_populates='sows_')
    buildings: List['Buildings'] = Relationship(back_populates='sow')
    feed_sows: List['FeedSows'] = Relationship(back_populates='sow')
    labour: List['Labour'] = Relationship(back_populates='sow')
    machines: List['Machines'] = Relationship(back_populates='sow')


class SowsPerformance(SQLModel, table=True):
    __tablename__ = 'sows_performance'
    __table_args__ = (
        ForeignKeyConstraint(['general_id'], ['general_farm.general_id'], name='sows_performance_general_id_fkey'),
        PrimaryKeyConstraint('sows_performance_id', name='sows_performance_pkey')
    )

    sows_performance_id: Optional[int] = Field(default=None, sa_column=Column('sows_performance_id', Integer, primary_key=True))
    piglets_born_alive: Optional[int] = Field(default=None, sa_column=Column('piglets_born_alive', Integer, comment='piglets/sow/year'))
    cycles_per_sow_year: Optional[int] = Field(default=None, sa_column=Column('cycles_per_sow_year', Integer, comment='piglets/sow/year'))
    avg_gestation_period: Optional[Decimal] = Field(default=None, sa_column=Column('avg_gestation_period', Numeric, comment='days'))
    duration_suckling_per_farrowing: Optional[Decimal] = Field(default=None, sa_column=Column('duration_suckling_per_farrowing', Numeric, comment='days'))
    dry_sow_days: Optional[int] = Field(default=None, sa_column=Column('dry_sow_days', Integer, comment='days'))
    rate_insuccesful_insemination: Optional[Decimal] = Field(default=None, sa_column=Column('rate_insuccesful_insemination', Numeric(5, 4), comment='%'))
    weaning_weights: Optional[Decimal] = Field(default=None, sa_column=Column('weaning_weights', Numeric, comment='kg LW per head'))
    cull_rate_sows: Optional[Decimal] = Field(default=None, sa_column=Column('cull_rate_sows', Numeric(5, 4), comment='%'))
    cull_rate_boars: Optional[Decimal] = Field(default=None, sa_column=Column('cull_rate_boars', Numeric(5, 4), comment='%'))
    fraction_own_replacement: Optional[Decimal] = Field(default=None, sa_column=Column('fraction_own_replacement', Numeric(5, 4), comment='%'))
    annual_sow_mortality: Optional[Decimal] = Field(default=None, sa_column=Column('annual_sow_mortality', Numeric(5, 4), comment='%'))
    annual_boar_mortality: Optional[Decimal] = Field(default=None, sa_column=Column('annual_boar_mortality', Numeric(5, 4), comment='%'))
    piglet_mortality_weaning: Optional[Decimal] = Field(default=None, sa_column=Column('piglet_mortality_weaning', Numeric(5, 4), comment='%'))
    piglet_mortality_rearing: Optional[Decimal] = Field(default=None, sa_column=Column('piglet_mortality_rearing', Numeric(5, 4), comment='%'))
    piglets_weaned: Optional[Decimal] = Field(default=None, sa_column=Column('piglets_weaned', Numeric, comment='piglets/sow/year'))
    avg_duration_piglet_rearing: Optional[Decimal] = Field(default=None, sa_column=Column('avg_duration_piglet_rearing', Numeric, comment='days'))
    reared_piglets: Optional[Decimal] = Field(default=None, sa_column=Column('reared_piglets', Numeric, comment='piglets/sow/year'))
    general_id: Optional[int] = Field(default=None, sa_column=Column('general_id', Integer))
    year: Optional[int] = Field(default=None, sa_column=Column('year', Integer))

    general: Optional['GeneralFarm'] = Relationship(back_populates='sows_performance')


class VarCostFinishing(SQLModel, table=True):
    __tablename__ = 'var_cost_finishing'
    __table_args__ = (
        ForeignKeyConstraint(['general_id'], ['general_farm.general_id'], name='var_cost_finishing_general_id_fkey'),
        PrimaryKeyConstraint('var_cost_fin_id', name='var_cost_finishing_pkey')
    )

    var_cost_fin_id: Optional[int] = Field(default=None, sa_column=Column('var_cost_fin_id', Integer, primary_key=True))
    veterinary_medicine_supplies: Optional[Decimal] = Field(default=None, sa_column=Column('veterinary_medicine_supplies', Numeric, comment='C/head'))
    disinfection: Optional[Decimal] = Field(default=None, sa_column=Column('disinfection', Numeric, comment='C/head'))
    energy: Optional[Decimal] = Field(default=None, sa_column=Column('energy', Numeric, comment='C/head'))
    water: Optional[Decimal] = Field(default=None, sa_column=Column('water', Numeric, comment='C/head'))
    manure_cost: Optional[Decimal] = Field(default=None, sa_column=Column('manure_cost', Numeric, comment='C/head'))
    transport_cost: Optional[Decimal] = Field(default=None, sa_column=Column('transport_cost', Numeric, comment='C/head'))
    specialised_pig_advisor: Optional[Decimal] = Field(default=None, sa_column=Column('specialised_pig_advisor', Numeric, comment='C/head'))
    animal_disease_levy: Optional[Decimal] = Field(default=None, sa_column=Column('animal_disease_levy', Numeric, comment='C/head'))
    carcass_disposal: Optional[Decimal] = Field(default=None, sa_column=Column('carcass_disposal', Numeric, comment='C/head'))
    maintenance: Optional[Decimal] = Field(default=None, sa_column=Column('maintenance', Numeric, comment='C/head'))
    general_id: Optional[int] = Field(default=None, sa_column=Column('general_id', Integer))
    year: Optional[int] = Field(default=None, sa_column=Column('year', Integer))

    general: Optional['GeneralFarm'] = Relationship(back_populates='var_cost_finishing')


class VariableCostsSows(SQLModel, table=True):
    __tablename__ = 'variable_costs_sows'
    __table_args__ = (
        ForeignKeyConstraint(['general_id'], ['general_farm.general_id'], name='variable_costs_sows_general_id_fkey'),
        PrimaryKeyConstraint('var_cost_id', name='variable_costs_sows_pkey')
    )

    var_cost_id: Optional[int] = Field(default=None, sa_column=Column('var_cost_id', Integer, primary_key=True))
    veterinary_medicine_supplies: Optional[Decimal] = Field(default=None, sa_column=Column('veterinary_medicine_supplies', Numeric, comment='C/head'))
    artificial_insemination: Optional[Decimal] = Field(default=None, sa_column=Column('artificial_insemination', Numeric, comment='C/head'))
    pregnancy_check: Optional[Decimal] = Field(default=None, sa_column=Column('pregnancy_check', Numeric, comment='C/head'))
    disinfection: Optional[Decimal] = Field(default=None, sa_column=Column('disinfection', Numeric, comment='C/head'))
    energy: Optional[Decimal] = Field(default=None, sa_column=Column('energy', Numeric, comment='C/head'))
    water: Optional[Decimal] = Field(default=None, sa_column=Column('water', Numeric, comment='C/head'))
    manure_costs: Optional[Decimal] = Field(default=None, sa_column=Column('manure_costs', Numeric, comment='C/head'))
    transport_costs: Optional[Decimal] = Field(default=None, sa_column=Column('transport_costs', Numeric, comment='C/head'))
    specialised_advisors: Optional[Decimal] = Field(default=None, sa_column=Column('specialised_advisors', Numeric, comment='C/head'))
    animal_disease_levy: Optional[Decimal] = Field(default=None, sa_column=Column('animal_disease_levy', Numeric, comment='C/head'))
    carcass_disposal: Optional[Decimal] = Field(default=None, sa_column=Column('carcass_disposal', Numeric, comment='C/head'))
    sow_planner: Optional[Decimal] = Field(default=None, sa_column=Column('sow_planner', Numeric, comment='C/head'))
    maintenance: Optional[Decimal] = Field(default=None, sa_column=Column('maintenance', Numeric, comment='C/head'))
    others: Optional[Decimal] = Field(default=None, sa_column=Column('others', Numeric, comment='C/head'))
    general_id: Optional[int] = Field(default=None, sa_column=Column('general_id', Integer))
    year: Optional[int] = Field(default=None, sa_column=Column('year', Integer))

    general: Optional['GeneralFarm'] = Relationship(back_populates='variable_costs_sows')


class Buildings(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['finishing_id'], ['pig_finishing.finishing_id'], name='buildings_finishing_id_fkey'),
        ForeignKeyConstraint(['general_id'], ['general_farm.general_id'], name='buildings_general_id_fkey'),
        ForeignKeyConstraint(['sow_id'], ['sows.sows_id'], name='buildings_sow_id_fkey'),
        PrimaryKeyConstraint('buildings_id', name='buildings_pkey')
    )

    buildings_id: Optional[int] = Field(default=None, sa_column=Column('buildings_id', Integer, primary_key=True))
    general_id: Optional[int] = Field(default=None, sa_column=Column('general_id', Integer))
    sow_id: Optional[int] = Field(default=None, sa_column=Column('sow_id', Integer))
    finishing_id: Optional[int] = Field(default=None, sa_column=Column('finishing_id', Integer))
    sum_annual_depreciation: Optional[Decimal] = Field(default=None, sa_column=Column('sum_annual_depreciation', Numeric, comment='C'))
    sum_book_values: Optional[Decimal] = Field(default=None, sa_column=Column('sum_book_values', Numeric, comment='C'))
    building_name: Optional[str] = Field(default=None, sa_column=Column('building_name', String(255)))
    purchase_year: Optional[date] = Field(default=None, sa_column=Column('purchase_year', Date))
    purchase_price: Optional[Decimal] = Field(default=None, sa_column=Column('purchase_price', Numeric, comment='C/piece'))
    utilization_period: Optional[Decimal] = Field(default=None, sa_column=Column('utilization_period', Numeric, comment='for tax'))
    salvage_value: Optional[Decimal] = Field(default=None, sa_column=Column('salvage_value', Numeric, comment='C/piece'))
    replacement_value: Optional[Decimal] = Field(default=None, sa_column=Column('replacement_value', Numeric, comment='C/piece'))
    enterprise_codes: Optional[int] = Field(default=None, sa_column=Column('enterprise_codes', Integer))
    year: Optional[int] = Field(default=None, sa_column=Column('year', Integer))

    finishing: Optional['PigFinishing'] = Relationship(back_populates='buildings')
    general: Optional['GeneralFarm'] = Relationship(back_populates='buildings')
    sow: Optional['Sows'] = Relationship(back_populates='buildings')


class FeedSows(SQLModel, table=True):
    __tablename__ = 'feed_sows'
    __table_args__ = (
        ForeignKeyConstraint(['finishing_id'], ['pig_finishing.finishing_id'], name='feed_sows_finishing_id_fkey'),
        ForeignKeyConstraint(['general_id'], ['general_farm.general_id'], name='feed_sows_general_id_fkey'),
        ForeignKeyConstraint(['sow_id'], ['sows.sows_id'], name='feed_sows_sow_id_fkey'),
        PrimaryKeyConstraint('feed_id', name='feed_sows_pkey')
    )

    feed_id: Optional[int] = Field(default=None, sa_column=Column('feed_id', Integer, primary_key=True))
    general_id: Optional[int] = Field(default=None, sa_column=Column('general_id', Integer))
    sow_id: Optional[int] = Field(default=None, sa_column=Column('sow_id', Integer))
    finishing_id: Optional[int] = Field(default=None, sa_column=Column('finishing_id', Integer))
    sows_gestation_feed: Optional[Decimal] = Field(default=None, sa_column=Column('sows_gestation_feed', Numeric, comment='kg/animal and year'))
    sows_lactation_feed: Optional[Decimal] = Field(default=None, sa_column=Column('sows_lactation_feed', Numeric, comment='kg/animal and year'))
    sows_total_feed_daily: Optional[Decimal] = Field(default=None, sa_column=Column('sows_total_feed_daily', Numeric, comment='kg/animal and day'))
    sows_total_feed_yearly: Optional[Decimal] = Field(default=None, sa_column=Column('sows_total_feed_yearly', Numeric, comment='kg/year'))
    gilts_special_feed: Optional[str] = Field(default=None, sa_column=Column('gilts_special_feed', Enum('Special gilt feed', 'Mix of gestation and lactation feed', name='gilts_special_feed_t')))
    gilts_share_gestation_feed: Optional[Decimal] = Field(default=None, sa_column=Column('gilts_share_gestation_feed', Numeric(5, 4), comment='%'))
    gilts_share_lactation_feed: Optional[Decimal] = Field(default=None, sa_column=Column('gilts_share_lactation_feed', Numeric(5, 4), comment='%'))
    gilts_feed_quantity_yearly: Optional[Decimal] = Field(default=None, sa_column=Column('gilts_feed_quantity_yearly', Numeric, comment='kg/animal and year'))
    gilts_total_feed_yearly: Optional[Decimal] = Field(default=None, sa_column=Column('gilts_total_feed_yearly', Numeric, comment='kg/year'))
    boars_special_feed: Optional[str] = Field(default=None, sa_column=Column('boars_special_feed', Enum('Special Boar feed', 'Mix of gestation and lactation feed', name='boars_special_feed_t')))
    boars_share_gestation_feed: Optional[Decimal] = Field(default=None, sa_column=Column('boars_share_gestation_feed', Numeric(5, 4), comment='%'))
    boars_share_lactation_feed: Optional[Decimal] = Field(default=None, sa_column=Column('boars_share_lactation_feed', Numeric(5, 4), comment='%'))
    boars_feed_quantity_yearly: Optional[Decimal] = Field(default=None, sa_column=Column('boars_feed_quantity_yearly', Numeric, comment='kg/animal and year'))
    boars_total_feed_yearly: Optional[Decimal] = Field(default=None, sa_column=Column('boars_total_feed_yearly', Numeric, comment='kg/year'))
    piglet_feed_1: Optional[Decimal] = Field(default=None, sa_column=Column('piglet_feed_1', Numeric, comment='kg/animal'))
    piglet_feed_2: Optional[Decimal] = Field(default=None, sa_column=Column('piglet_feed_2', Numeric, comment='kg/animal'))
    piglet_total_feed_yearly: Optional[Decimal] = Field(default=None, sa_column=Column('piglet_total_feed_yearly', Numeric, comment='kg/year'))
    year: Optional[int] = Field(default=None, sa_column=Column('year', Integer))

    finishing: Optional['PigFinishing'] = Relationship(back_populates='feed_sows')
    general: Optional['GeneralFarm'] = Relationship(back_populates='feed_sows')
    sow: Optional['Sows'] = Relationship(back_populates='feed_sows')
    cash_crops: List['CashCrops'] = Relationship(back_populates='feed')


class Labour(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['finishing_id'], ['pig_finishing.finishing_id'], name='labour_finishing_id_fkey'),
        ForeignKeyConstraint(['general_id'], ['general_farm.general_id'], name='labour_general_id_fkey'),
        ForeignKeyConstraint(['sow_id'], ['sows.sows_id'], name='labour_sow_id_fkey'),
        PrimaryKeyConstraint('labour_id', name='labour_pkey')
    )

    labour_id: Optional[int] = Field(default=None, sa_column=Column('labour_id', Integer, primary_key=True))
    general_id: Optional[int] = Field(default=None, sa_column=Column('general_id', Integer))
    sow_id: Optional[int] = Field(default=None, sa_column=Column('sow_id', Integer))
    finishing_id: Optional[int] = Field(default=None, sa_column=Column('finishing_id', Integer))
    type: Optional[str] = Field(default=None, sa_column=Column('type', Enum('Manager', 'Executive Staff', 'Tractor Driver', 'Pigman', 'Casual Labour', 'Family Labour', 'Other', name='type_t')))
    labor_units: Optional[Decimal] = Field(default=None, sa_column=Column('labor_units', Numeric, comment='Number(Anzahl)'))
    working_hours: Optional[Decimal] = Field(default=None, sa_column=Column('working_hours', Numeric, comment='per person per year'))
    annual_wage_incl_sidecosts: Optional[Decimal] = Field(default=None, sa_column=Column('annual_wage_incl_sidecosts', Numeric, comment='per person'))
    enterprise_code: Optional[int] = Field(default=None, sa_column=Column('enterprise_code', Integer))
    year: Optional[int] = Field(default=None, sa_column=Column('year', Integer))

    finishing: Optional['PigFinishing'] = Relationship(back_populates='labour')
    general: Optional['GeneralFarm'] = Relationship(back_populates='labour')
    sow: Optional['Sows'] = Relationship(back_populates='labour')


class Machines(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['finishing_id'], ['pig_finishing.finishing_id'], name='machines_finishing_id_fkey'),
        ForeignKeyConstraint(['general_id'], ['general_farm.general_id'], name='machines_general_id_fkey'),
        ForeignKeyConstraint(['sow_id'], ['sows.sows_id'], name='machines_sow_id_fkey'),
        PrimaryKeyConstraint('machines_id', name='machines_pkey')
    )

    machines_id: Optional[int] = Field(default=None, sa_column=Column('machines_id', Integer, primary_key=True))
    general_id: Optional[int] = Field(default=None, sa_column=Column('general_id', Integer))
    sow_id: Optional[int] = Field(default=None, sa_column=Column('sow_id', Integer))
    finishing_id: Optional[int] = Field(default=None, sa_column=Column('finishing_id', Integer))
    sum_annual_depreciation: Optional[Decimal] = Field(default=None, sa_column=Column('sum_annual_depreciation', Numeric, comment='C'))
    sum_book_values: Optional[Decimal] = Field(default=None, sa_column=Column('sum_book_values', Numeric, comment='C'))
    tractors: Optional[str] = Field(default=None, sa_column=Column('tractors', String(255)))
    purchase_year: Optional[date] = Field(default=None, sa_column=Column('purchase_year', Date))
    purchase_price: Optional[Decimal] = Field(default=None, sa_column=Column('purchase_price', Numeric, comment='C/piece'))
    utilization_period: Optional[Decimal] = Field(default=None, sa_column=Column('utilization_period', Numeric, comment='economically'))
    salvage_value: Optional[Decimal] = Field(default=None, sa_column=Column('salvage_value', Numeric, comment='C/piece'))
    replacement_value: Optional[Decimal] = Field(default=None, sa_column=Column('replacement_value', Numeric, comment='C/piece'))
    enterprise_code: Optional[int] = Field(default=None, sa_column=Column('enterprise_code', Integer))
    year: Optional[int] = Field(default=None, sa_column=Column('year', Integer))

    finishing: Optional['PigFinishing'] = Relationship(back_populates='machines')
    general: Optional['GeneralFarm'] = Relationship(back_populates='machines')
    sow: Optional['Sows'] = Relationship(back_populates='machines')


class CashCrops(SQLModel, table=True):
    __tablename__ = 'cash_crops'
    __table_args__ = (
        ForeignKeyConstraint(['feed_id'], ['feed_sows.feed_id'], name='cash_crops_feed_id_fkey'),
        ForeignKeyConstraint(['general_id'], ['general_farm.general_id'], name='cash_crops_general_id_fkey'),
        PrimaryKeyConstraint('crops_id', name='cash_crops_pkey')
    )

    crops_id: Optional[int] = Field(default=None, sa_column=Column('crops_id', Integer, primary_key=True))
    general_id: Optional[int] = Field(default=None, sa_column=Column('general_id', Integer))
    feed_id: Optional[int] = Field(default=None, sa_column=Column('feed_id', Integer))
    crop_name: Optional[str] = Field(default=None, sa_column=Column('crop_name', String(50), comment='Set aside, Corn, Wheat, Barley'))
    year: Optional[int] = Field(default=None, sa_column=Column('year', Integer))

    feed: Optional['FeedSows'] = Relationship(back_populates='cash_crops')
    general: Optional['GeneralFarm'] = Relationship(back_populates='cash_crops')
    land_use: List['LandUse'] = Relationship(back_populates='crop')
    var_cost_crop: List['VarCostCrop'] = Relationship(back_populates='crop')


class LandUse(SQLModel, table=True):
    __tablename__ = 'land_use'
    __table_args__ = (
        ForeignKeyConstraint(['crop_id'], ['cash_crops.crops_id'], name='land_use_crop_id_fkey'),
        ForeignKeyConstraint(['general_id'], ['general_farm.general_id'], name='land_use_general_id_fkey'),
        PrimaryKeyConstraint('landuse_id', name='land_use_pkey')
    )

    landuse_id: Optional[int] = Field(default=None, sa_column=Column('landuse_id', Integer, primary_key=True))
    crop_name: Optional[str] = Field(default=None, sa_column=Column('crop_name', String(50), comment='Set aside, Corn, Wheat, Barley'))
    acerage: Optional[Decimal] = Field(default=None, sa_column=Column('acerage', Numeric, comment='ha'))
    net_yield: Optional[Decimal] = Field(default=None, sa_column=Column('net_yield', Numeric, comment='t/ha'))
    dry_matter: Optional[Decimal] = Field(default=None, sa_column=Column('dry_matter', Numeric, comment='0,0x'))
    price: Optional[Decimal] = Field(default=None, sa_column=Column('price', Numeric, comment='C/t'))
    cap_dir_paym: Optional[Decimal] = Field(default=None, sa_column=Column('cap_dir_paym', Numeric, comment='C/ha'))
    other_dir_paym: Optional[Decimal] = Field(default=None, sa_column=Column('other_dir_paym', Numeric, comment='C/ha'))
    enterprise_code: Optional[int] = Field(default=None, sa_column=Column('enterprise_code', Integer))
    crop_id: Optional[int] = Field(default=None, sa_column=Column('crop_id', Integer))
    general_id: Optional[int] = Field(default=None, sa_column=Column('general_id', Integer))
    year: Optional[int] = Field(default=None, sa_column=Column('year', Integer))

    crop: Optional['CashCrops'] = Relationship(back_populates='land_use')
    general: Optional['GeneralFarm'] = Relationship(back_populates='land_use')


class VarCostCrop(SQLModel, table=True):
    __tablename__ = 'var_cost_crop'
    __table_args__ = (
        ForeignKeyConstraint(['crop_id'], ['cash_crops.crops_id'], name='var_cost_crop_crop_id_fkey'),
        ForeignKeyConstraint(['general_id'], ['general_farm.general_id'], name='var_cost_crop_general_id_fkey'),
        PrimaryKeyConstraint('var_cost_crop_id', name='var_cost_crop_pkey')
    )

    var_cost_crop_id: Optional[int] = Field(default=None, sa_column=Column('var_cost_crop_id', Integer, primary_key=True))
    crop_name: Optional[str] = Field(default=None, sa_column=Column('crop_name', String(50), comment='Set aside, Corn, Wheat, Barley'))
    seeds: Optional[Decimal] = Field(default=None, sa_column=Column('seeds', Numeric, comment='C/ha'))
    fertilizer: Optional[Decimal] = Field(default=None, sa_column=Column('fertilizer', Numeric, comment='C/ha'))
    herbicides: Optional[Decimal] = Field(default=None, sa_column=Column('herbicides', Numeric, comment='C/ha'))
    fungicide: Optional[Decimal] = Field(default=None, sa_column=Column('fungicide', Numeric, comment='C/ha'))
    contract_labor: Optional[Decimal] = Field(default=None, sa_column=Column('contract_labor', Numeric, comment='C/ha'))
    energy: Optional[Decimal] = Field(default=None, sa_column=Column('energy', Numeric, comment='C/ha'))
    other: Optional[Decimal] = Field(default=None, sa_column=Column('other', Numeric, comment='C/ha'))
    crop_id: Optional[int] = Field(default=None, sa_column=Column('crop_id', Integer))
    general_id: Optional[int] = Field(default=None, sa_column=Column('general_id', Integer))
    year: Optional[int] = Field(default=None, sa_column=Column('year', Integer))

    crop: Optional['CashCrops'] = Relationship(back_populates='var_cost_crop')
    general: Optional['GeneralFarm'] = Relationship(back_populates='var_cost_crop')
