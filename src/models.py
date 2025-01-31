import datetime
import decimal
from typing import Optional
from sqlmodel import Field, SQLModel
from enum import Enum
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID
from pydantic import Json, UUID4

GiltsSpecialFeedT = Enum(
    value='GiltsSpecialFeedT',
    names=[
        ('Mix of gestation and lactation feed', 'Mix of gestation and lactation feed'),
        ('Special gilt feed', 'Special gilt feed')
    ]
)

BoarsSpecialFeedT = Enum(
    value='BoarsSpecialFeedT',
    names=[
        ('Mix of gestation and lactation feed', 'Mix of gestation and lactation feed'),
        ('Special Boar feed', 'Special Boar feed')
    ]
)

TypeT = Enum(
    value='TypeT',
    names=[
        ('Casual Labour', 'Casual Labour'),
        ('Executive Staff', 'Executive Staff'),
        ('Family Labour', 'Family Labour'),
        ('Manager', 'Manager'),
        ('Other', 'Other'),
        ('Pigman', 'Pigman'),
        ('Tractor Driver', 'Tractor Driver')
    ]
)

ProductionSystemT = Enum(
    value='ProductionSystemT',
    names=[
        ('additional boar finishing', 'additional boar finishing'),
        ('normal pig finishing', 'normal pig finishing')
    ]
)

ProductionCyleT = Enum(
    value='ProductionCyleT',
    names=[
        ('all-in all-out by barn', 'all-in all-out by barn'),
        ('continuous system', 'continuous system')
    ]
)

ProductionsystemT = Enum(
    value='ProductionsystemT',
    names=[
        ('closed system', 'closed system'),
        ('pure piglet rearing', 'pure piglet rearing'),
        ('system piglet sales  ( approx. 8kg)', 'system piglet sales  ( approx. 8kg)'),
        ('weaner sales  ( approx. 25-30kg)', 'weaner sales  ( approx. 25-30kg)')
    ]
)

ProductionRhythmT = Enum(
    value='ProductionRhythmT',
    names=[
        ('1-week rhythm', '1-week rhythm'),
        ('2-week rhythm', '2-week rhythm'),
        ('3-week rhythm', '3-week rhythm'),
        ('4-week rhythm', '4-week rhythm'),
        ('none or other rhythm', 'none or other rhythm')
    ]
)

FertilizerTypeT = Enum(
    value='FertilizerTypeT',
    names=[
        ('mineral', 'mineral'),
        ('organic', 'organic')
    ]
)

FertilizerNameT = Enum(
    value='FertilizerNameT',
    names=[
        ('calcium', 'calcium'),
        ('nitrogen', 'nitrogen'),
        ('others', 'others'),
        ('phosphorus', 'phosphorus'),
        ('potash', 'potash')
    ]
)

CerealTypeT = Enum(
    value='CerealTypeT',
    names=[
        ('barley', 'barley'),
        ('bought-in forage', 'bought-in forage'),
        ('concentrates', 'concentrates'),
        ('corn', 'corn'),
        ('milk replacer', 'milk replacer'),
        ('minerals', 'minerals'),
        ('oils', 'oils'),
        ('set-aside', 'set-aside'),
        ('wheat', 'wheat')
    ]
)

ProductionT = Enum(
    value='ProductionT',
    names=[
        ('finishing', 'finishing'),
        ('sows', 'sows')
    ]
)

FeedSourcesT = Enum(
    value='FeedSourcesT',
    names=[
        ('Bought feed', 'Bought feed'),
        ('Self produced', 'Self produced')
    ]
)

FeedTypeT = Enum(
    value='FeedTypeT',
    names=[
        ('Finishing feed 1', 'Finishing feed 1'),
        ('Finishing feed 2', 'Finishing feed 2'),
        ('Finishing feed 3', 'Finishing feed 3'),
        ('Gestation feed', 'Gestation feed'),
        ('Lactation feed', 'Lactation feed'),
        ('Piglet feed 1', 'Piglet feed 1'),
        ('Piglet feed 2', 'Piglet feed 2'),
        ('Special boar feed', 'Special boar feed'),
        ('Special gilt feed', 'Special gilt feed')
    ]
)


class GeneralFarm(SQLModel, table=True):

    __tablename__ = 'general_farm'

    id: UUID4 = Field(unique=True, sa_type=UUID)
    general_id: Optional[UUID4] = Field(default=None, primary_key=True, unique=True, sa_type=UUID)
    firstname: Optional[str]
    lastname: Optional[str]
    username: Optional[str]
    email: Optional[str]
    password: Optional[str]
    land: Optional[str]
    region: Optional[str]
    currency: Optional[str]
    legal_status: Optional[str]
    reference_year_data: Optional[int]
    cash_crop: Optional[bool]
    sows: Optional[bool]
    pig_finishing: Optional[bool]
    year: Optional[int]
    farm_id: Optional[str]
    scenario_id: Optional[str]
    scenario_name: Optional[str]
    farm_name: Optional[str]
    network_pig: Optional[bool]
    network_beef: Optional[bool]
    network_crop: Optional[bool]
    network_horticulture: Optional[bool]
    network_fish: Optional[bool]
    network_poultry: Optional[bool]


class Buildings(SQLModel, table=True):

    __tablename__ = 'buildings'

    id: UUID4 = Field(unique=True, sa_type=UUID)
    buildings_id: Optional[UUID4] = Field(default=None, primary_key=True, unique=True, sa_type=UUID)
    general_id: UUID4 = Field(sa_type=UUID)
    sow_id: Optional[UUID4] = Field(sa_type=UUID)
    finishing_id: Optional[int]
    sum_annual_depreciation: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    sum_book_values: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    building_name: Optional[str]
    purchase_year: Optional[int]
    purchase_price: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    utilization_period: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    salvage_value: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    replacement_value: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    enterprise_codes: Optional[int]
    year: Optional[int]


class FeedSows(SQLModel, table=True):

    __tablename__ = 'feed_sows'

    id: UUID4 = Field(unique=True, sa_type=UUID)
    feed_id: Optional[UUID4] = Field(default=None, primary_key=True, unique=True, sa_type=UUID)
    general_id: UUID4 = Field(sa_type=UUID)
    sow_id: Optional[UUID4] = Field(sa_type=UUID)
    finishing_id: Optional[int]
    sows_gestation_feed: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    sows_lactation_feed: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    sows_total_feed_daily: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    sows_total_feed_yearly: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    gilts_special_feed: Optional[GiltsSpecialFeedT] = Field(sa_type=sa.Enum(GiltsSpecialFeedT))
    gilts_share_gestation_feed: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric(5,4))
    gilts_share_lactation_feed: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric(5,4))
    gilts_feed_quantity_yearly: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    gilts_total_feed_yearly: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    boars_special_feed: Optional[BoarsSpecialFeedT] = Field(sa_type=sa.Enum(BoarsSpecialFeedT))
    boars_share_gestation_feed: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric(5,4))
    boars_share_lactation_feed: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric(5,4))
    boars_feed_quantity_yearly: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    boars_total_feed_yearly: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    piglet_feed_1: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    piglet_feed_2: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    piglet_feed_quantity_yearly: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    piglet_total_feed_yearly: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    year: Optional[int]


class Machines(SQLModel, table=True):

    __tablename__ = 'machines'

    id: UUID4 = Field(unique=True, sa_type=UUID)
    machines_id: Optional[UUID4] = Field(default=None, primary_key=True, unique=True, sa_type=UUID)
    general_id: UUID4 = Field(sa_type=UUID)
    sow_id: Optional[UUID4] = Field(sa_type=UUID)
    finishing_id: Optional[int]
    sum_annual_depreciation: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    sum_book_values: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    name: Optional[str]
    purchase_year: Optional[int]
    purchase_price: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    utilization_period: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    salvage_value: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    replacement_value: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    enterprise_code: Optional[int]
    year: Optional[int]


class Labour(SQLModel, table=True):

    __tablename__ = 'labour'

    id: UUID4 = Field(unique=True, sa_type=UUID)
    labour_id: Optional[UUID4] = Field(default=None, primary_key=True, unique=True, sa_type=UUID)
    general_id: UUID4 = Field(sa_type=UUID)
    sow_id: Optional[UUID4] = Field(sa_type=UUID)
    finishing_id: Optional[int]
    type: Optional[TypeT] = Field(sa_type=sa.Enum(TypeT))
    name: Optional[str]
    labor_units: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    working_hours: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    annual_wage_incl_sidecosts: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    enterprise_code: Optional[int]
    year: Optional[int]


class CashCrops(SQLModel, table=True):

    __tablename__ = 'cash_crops'

    id: UUID4 = Field(unique=True, sa_type=UUID)
    crops_id: Optional[UUID4] = Field(default=None, primary_key=True, unique=True, sa_type=UUID)
    general_id: UUID4 = Field(sa_type=UUID)
    feed_id: Optional[UUID4] = Field(sa_type=UUID)
    crop_name: Optional[str]
    year: Optional[int]


class PigFinishing(SQLModel, table=True):

    __tablename__ = 'pig_finishing'

    id: UUID4 = Field(unique=True, sa_type=UUID)
    finishing_id: Optional[int] = Field(default=None, primary_key=True, unique=True)
    general_id: UUID4 = Field(sa_type=UUID)
    production_system: Optional[ProductionSystemT] = Field(sa_type=sa.Enum(ProductionSystemT))
    production_cyle: Optional[ProductionCyleT] = Field(sa_type=sa.Enum(ProductionCyleT))
    animal_places: Optional[int]
    no_sold_pigs_gi_ba: Optional[int]
    no_sold_em_ic: Optional[int]
    share_gi_pigs: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric(5,4))
    year: Optional[int]


class Sows(SQLModel, table=True):

    __tablename__ = 'sows'

    id: UUID4 = Field(unique=True, sa_type=UUID)
    sows_id: Optional[UUID4] = Field(default=None, primary_key=True, unique=True, sa_type=UUID)
    general_id: UUID4 = Field(sa_type=UUID)
    productionsystem: Optional[ProductionsystemT] = Field(sa_type=sa.Enum(ProductionsystemT))
    production_rhythm: Optional[ProductionRhythmT] = Field(sa_type=sa.Enum(ProductionRhythmT))
    no_sows_mated_gilts: Optional[int]
    no_unserved_gilts: Optional[int]
    no_boars: Optional[int]
    total_no_sows_gilts: Optional[int]
    year: Optional[int]


class VariableCostsSows(SQLModel, table=True):

    __tablename__ = 'variable_costs_sows'

    id: UUID4 = Field(unique=True, sa_type=UUID)
    var_cost_id: Optional[UUID4] = Field(default=None, primary_key=True, unique=True, sa_type=UUID)
    veterinary_medicine_supplies: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    artificial_insemination: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    pregnancy_check: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    disinfection: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    energy: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    water: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    manure_costs: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    transport_costs: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    specialised_advisors: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    animal_disease_levy: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    carcass_disposal: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    sow_planner: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    maintenance: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    others: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    general_id: UUID4 = Field(sa_type=UUID)
    year: Optional[int]


class FixCosts(SQLModel, table=True):

    __tablename__ = 'fix_costs'

    id: UUID4 = Field(unique=True, sa_type=UUID)
    fix_cost_id: Optional[UUID4] = Field(default=None, primary_key=True, unique=True, sa_type=UUID)
    feed_grinding_preparation: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    insurance: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    cleaning: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    others: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    general_id: UUID4 = Field(sa_type=UUID)
    year: Optional[int]


class SowsPerformance(SQLModel, table=True):

    __tablename__ = 'sows_performance'

    id: UUID4 = Field(unique=True, sa_type=UUID)
    sows_performance_id: Optional[UUID4] = Field(default=None, primary_key=True, unique=True, sa_type=UUID)
    piglets_born_alive: Optional[int]
    cycles_per_sow_year: Optional[int]
    avg_gestation_period: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    duration_suckling_per_farrowing: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    dry_sow_days: Optional[int]
    rate_insuccesful_insemination: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric(5,4))
    weaning_weights: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    cull_rate_sows: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric(5,4))
    cull_rate_boars: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric(5,4))
    fraction_own_replacement: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric(5,4))
    annual_sow_mortality: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric(5,4))
    annual_boar_mortality: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric(5,4))
    piglet_mortality_weaning: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric(5,4))
    piglet_mortality_rearing: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric(5,4))
    piglets_weaned: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    avg_duration_piglet_rearing: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    reared_piglets: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    general_id: UUID4 = Field(sa_type=UUID)
    year: Optional[int]


class LiabilitiesInterestRates(SQLModel, table=True):

    __tablename__ = 'liabilities_interest_rates'

    id: UUID4 = Field(unique=True, sa_type=UUID)
    liabilities_id: Optional[UUID4] = Field(default=None, primary_key=True, unique=True, sa_type=UUID)
    long_term_loans: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric(5,4))
    medium_term_loans: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric(5,4))
    short_term_loans: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric(5,4))
    circulating_capital_overdraft: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric(5,4))
    savings: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric(5,4))
    total_liabilities: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    total_long_term_loans: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    total_medium_term_loans: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    total_short_term_loans: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    perc_debt_total_assets: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric(5,4))
    general_id: UUID4 = Field(sa_type=UUID)
    year: Optional[int]


class OverheadCosts(SQLModel, table=True):

    __tablename__ = 'overhead_costs'

    id: UUID4 = Field(unique=True, sa_type=UUID)
    overhead_id: Optional[UUID4] = Field(default=None, primary_key=True, unique=True, sa_type=UUID)
    land_improvements: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    maintenance_machinery: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    maintenance_buildings: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    contracted_labour_machinery_association: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    diesel_vehicles: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    diesel_heating_irrigation: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    gasoline: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    gas: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    electricity: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    water_fresh_waste_water_fees: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    farm_insurance: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    invalidity_insurance: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    taxes_fees: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    advisory_services_trainings: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    accounting: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    office_communication_subs: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    others: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    general_id: UUID4 = Field(sa_type=UUID)
    year: Optional[int]


class DirectAidFromFarm(SQLModel, table=True):

    __tablename__ = 'direct_aid_from_farm'

    id: UUID4 = Field(unique=True, sa_type=UUID)
    direct_aid_id: Optional[UUID4] = Field(default=None, primary_key=True, unique=True, sa_type=UUID)
    compensatory_allovance_disadvantage_area: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    general_id: UUID4 = Field(sa_type=UUID)
    year: Optional[int]


class AceragePrices(SQLModel, table=True):

    __tablename__ = 'acerage_prices'

    id: UUID4 = Field(unique=True, sa_type=UUID)
    acerage_id: Optional[UUID4] = Field(default=None, primary_key=True, unique=True, sa_type=UUID)
    land_type: Optional[str]
    own_land: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    rented_land: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    rent_existing_contracts: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    rent_new_contracts: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    market_value: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    general_id: UUID4 = Field(sa_type=UUID)
    year: Optional[int]


class LandUse(SQLModel, table=True):

    __tablename__ = 'land_use'

    id: UUID4 = Field(unique=True, sa_type=UUID)
    landuse_id: Optional[UUID4] = Field(default=None, primary_key=True, unique=True, sa_type=UUID)
    crop_name: Optional[str]
    acerage: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    net_yield: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    dry_matter: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    price: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    cap_dir_paym: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    other_dir_paym: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    enterprise_code: Optional[int]
    crop_id: Optional[UUID4] = Field(sa_type=UUID)
    general_id: UUID4 = Field(sa_type=UUID)
    year: Optional[int]


class VarCostCrop(SQLModel, table=True):

    __tablename__ = 'var_cost_crop'

    id: UUID4 = Field(unique=True, sa_type=UUID)
    var_cost_crop_id: Optional[UUID4] = Field(default=None, primary_key=True, unique=True, sa_type=UUID)
    crop_name: Optional[str]
    seeds: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    fertilizer: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    herbicides: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    fungicide: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    contract_labor: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    energy: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    other: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    crop_id: Optional[UUID4] = Field(sa_type=UUID)
    general_id: UUID4 = Field(sa_type=UUID)
    year: Optional[int]


class FeedPricesDryMatter(SQLModel, table=True):

    __tablename__ = 'feed_prices_dry_matter'

    id: UUID4 = Field(unique=True, sa_type=UUID)
    feed_prices_id: Optional[UUID4] = Field(default=None, primary_key=True, unique=True, sa_type=UUID)
    feed_type: Optional[str]
    price_per_tonne: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    dry_matter_percent: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric(5,4))
    energy_mj: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    protein: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    text: Optional[str]
    concentrate: Optional[bool]
    general_id: UUID4 = Field(sa_type=UUID)
    year: Optional[int]


class SalesWeight(SQLModel, table=True):

    __tablename__ = 'sales_weight'

    id: UUID4 = Field(unique=True, sa_type=UUID)
    sales_weight_id: Optional[UUID4] = Field(default=None, primary_key=True, unique=True, sa_type=UUID)
    sales_weight_sows: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    sales_weight_boars: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    sales_weight_weaning_piglet: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    sales_weight_rearing_piglet: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    general_id: Optional[UUID4] = Field(sa_type=UUID)
    year: Optional[int]


class PricesSows(SQLModel, table=True):

    __tablename__ = 'prices_sows'

    id: UUID4 = Field(unique=True, sa_type=UUID)
    prices_sows_id: Optional[UUID4] = Field(default=None, primary_key=True, unique=True, sa_type=UUID)
    buying_gilts: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    buying_boars: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    selling_sow: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    selling_boar: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    selling_weaning_piglet: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    selling_rearing_piglet: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    proportion_weaned_pigs_sold: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    no_weaned_pigs_sold: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    general_id: UUID4 = Field(sa_type=UUID)
    year: Optional[int]


class PerformancePigFinishing(SQLModel, table=True):

    __tablename__ = 'performance_pig_finishing'

    id: UUID4 = Field(unique=True, sa_type=UUID)
    performance_fin_id: Optional[UUID4] = Field(default=None, primary_key=True, unique=True, sa_type=UUID)
    stalling_in_weight: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    stalling_in_weight_em_ic_piglets: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    avg_duration_finishing_period: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    cleaning_days_cycle: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    days_without_animals_instable: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    mortality: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric(5,4))
    avg_selling_weight_gi_ba: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    carcass_yield_gi_ba: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    lean_meat_from_gi_ba: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    index_points_autofom_gi_ba: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    avg_selling_weight_em_ic: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    carcass_yield_em_ic: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric(5,4))
    index_points_autofom_em_ic: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    avg_duration_finishing_period_em_ic: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    general_id: UUID4 = Field(sa_type=UUID)
    year: Optional[int]


class PricesFinishing(SQLModel, table=True):

    __tablename__ = 'prices_finishing'

    id: UUID4 = Field(unique=True, sa_type=UUID)
    prices_fin_id: Optional[UUID4] = Field(default=None, primary_key=True, unique=True, sa_type=UUID)
    buying_f_castpiglets: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    buying_piglets_for_finishing: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    selling_finishing_pigs_gi_ba: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    selling_finishing_pigs_em_ic: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    general_id: UUID4 = Field(sa_type=UUID)
    year: Optional[int]


class VarCostFinishing(SQLModel, table=True):

    __tablename__ = 'var_cost_finishing'

    id: UUID4 = Field(unique=True, sa_type=UUID)
    var_cost_fin_id: Optional[UUID4] = Field(default=None, primary_key=True, unique=True, sa_type=UUID)
    veterinary_medicine_supplies: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    disinfection: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    energy: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    water: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    manure_cost: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    transport_cost: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    specialised_pig_advisor: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    animal_disease_levy: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    carcass_disposal: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    maintenance: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    general_id: UUID4 = Field(sa_type=UUID)
    year: Optional[int]


class LaborAllocSowFinishing(SQLModel, table=True):

    __tablename__ = 'labor_alloc_sow_finishing'

    id: Optional[UUID4] = Field(default=None, primary_key=True, unique=True, sa_type=UUID)
    casual_labor_sow: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    family_labor_sow: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    casual_labor_finishing: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    family_labor_finishing: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    general_id: UUID4 = Field(sa_type=UUID)
    year: Optional[int]


class FeedingFinishing(SQLModel, table=True):

    __tablename__ = 'feeding_finishing'

    id: UUID4 = Field(unique=True, sa_type=UUID)
    feed_fin_id: Optional[UUID4] = Field(default=None, primary_key=True, unique=True, sa_type=UUID)
    proportion_finishing_feed_1: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric(5,4))
    proportion_finishing_feed_2: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric(5,4))
    proportion_finishing_feed_3: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric(5,4))
    amount_finishing_feed_1: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    amount_finishing_feed_2: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    amount_finishing_feed_3: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    total_amount_feed: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    general_id: UUID4 = Field(sa_type=UUID)
    year: Optional[int]


class Fertilizer(SQLModel, table=True):

    __tablename__ = 'fertilizer'

    id: UUID4 = Field(unique=True, sa_type=UUID)
    fertilizer_id: Optional[UUID4] = Field(default=None, primary_key=True, unique=True, sa_type=UUID)
    fertilizer_type: Optional[FertilizerTypeT] = Field(sa_type=sa.Enum(FertilizerTypeT))
    fertilizer_name: Optional[FertilizerNameT] = Field(sa_type=sa.Enum(FertilizerNameT))
    fertilizer_name_custom: Optional[str]
    amount: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    amount_unit: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    n_content_per_unit: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    general_id: UUID4 = Field(sa_type=UUID)
    year: Optional[int]


class Feeds(SQLModel, table=True):

    __tablename__ = 'feeds'

    id: Optional[UUID4] = Field(default=None, primary_key=True, unique=True, sa_type=UUID)
    cereal_type: Optional[CerealTypeT] = Field(sa_type=sa.Enum(CerealTypeT))
    dry_matter: Optional[float]
    xp: Optional[float]
    energy: Optional[float]


class FeedRation(SQLModel, table=True):

    __tablename__ = 'feed_ration'

    id: UUID4 = Field(unique=True, sa_type=UUID)
    feed_ration_id: Optional[UUID4] = Field(default=None, primary_key=True, unique=True, sa_type=UUID)
    production: Optional[ProductionT] = Field(sa_type=sa.Enum(ProductionT))
    feed_sources: Optional[FeedSourcesT] = Field(sa_type=sa.Enum(FeedSourcesT))
    feed_type: Optional[FeedTypeT] = Field(sa_type=sa.Enum(FeedTypeT))
    feed_share: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    total_amount_feed_used: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    general_id: UUID4 = Field(sa_type=UUID)
    year: Optional[int]
    feeds_id: Optional[UUID4] = Field(sa_type=UUID)


class FeedRationSows(SQLModel, table=True):

    __tablename__ = 'feed_ration_sows'

    id: UUID4 = Field(unique=True, sa_type=UUID)
    feed_ration_sows_id: Optional[UUID4] = Field(default=None, primary_key=True, unique=True, sa_type=UUID)
    gestation_feed: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    lactation_feed: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    special_gilt_feed: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    special_boar_feed: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    piglet_feed_1: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    piglet_feed_2: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    total_amount_feed_used: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    year: Optional[int]
    general_id: Optional[UUID4] = Field(sa_type=UUID)
    feeds_id: Optional[UUID4] = Field(sa_type=UUID)


class FeedRationFinishing(SQLModel, table=True):

    __tablename__ = 'feed_ration_finishing'

    id: UUID4 = Field(unique=True, sa_type=UUID)
    feed_ration_finishing_id: Optional[UUID4] = Field(default=None, primary_key=True, unique=True, sa_type=UUID)
    finishing_feed_1: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    finishing_feed_2: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    finishing_feed_3: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    total_amount_feed_used: Optional[decimal.Decimal] = Field(sa_type=sa.Numeric())
    year: Optional[int]
    general_id: Optional[UUID4] = Field(sa_type=UUID)
    feeds_id: Optional[UUID4] = Field(sa_type=UUID)
